from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import keras
import tensorflow as tf  
from rest_framework.permissions import AllowAny
from .serializers import PredictionInput
#from timeseries.saved_models import scaler, timeseries 
from django.conf import settings
import os
import pickle


model_path = r"Enter Location for timeseries.h5 file"
timeseries_model = tf.keras.models.load_model(model_path)

# Load the saved scaler
scaler_path = r"Enter Location for scaler.pkl file"
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

class PredictView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            
            serializer = PredictionInput(data=request.data, many=True)
            if serializer.is_valid():
                
                if len(serializer.validated_data) != 10:
                    return Response(
                        {'error': 'Exactly 10 timesteps are required for prediction.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                
                input_data = np.array([
                    [
                        timestep['Temp1'],
                        timestep['Press1'],
                        timestep['Temp2'],
                        timestep['Press2'],
                        timestep['Status']
                    ] for timestep in serializer.validated_data
                ])

                
                input_data = input_data.reshape(1, 10, -1)

                
                input_data_scaled = scaler.transform(input_data.reshape(-1, input_data.shape[-1]))
                input_data_scaled = input_data_scaled.reshape(1, 10, -1)

                
                predictions = timeseries_model.predict(input_data_scaled)

                
                predictions_flattened = predictions.reshape(-1, predictions.shape[-1])
                predictions_inverse = scaler.inverse_transform(predictions_flattened)

                
                for row in predictions_inverse:
                    row[-1] = round(row[-1])  

                
                column_names = ["Temp1", "Press1", "Temp2", "Press2", "Status"]
                predictions_with_names = [
                    {column: value for column, value in zip(column_names, row)}
                    for row in predictions_inverse
                ]

                return Response({'predictions': predictions_with_names}, status=status.HTTP_200_OK)
            
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
