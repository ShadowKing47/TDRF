from rest_framework import serializers
from .models import PredictionInput

class PredictionInput(serializers.ModelSerializer):
    
    class Meta:
        model = PredictionInput  
        fields = ['Temp1', 'Press1', 'Temp2', 'Press2', 'Status']  
        
    def __str__(self):
        return f"Temp1: {self.Temp1}, Press1: {self.Press1}, Temp2: {self.Temp2}, Press2: {self.Press2}, Status: {self.Status}"
