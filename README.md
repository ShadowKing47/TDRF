The Repository consists of a Tensorflow backed Timeseries Predictive model for Predicting the future temperature and Pressure of an electric Motor.
The model takes input of previous 10 Readings an provides output for the future timestamp

Step 1. Clone the repo 

Step 2. Install required Libraries using the following command : pip install ipykernel django djangorestframework tensorflow pandas numpy scikit-learn

Step 3.Open powershell and run command : python manage.py runserver

step 5.In views.py/timeseries/myproject , mention the location for the following files : timeseries.h5, scaler.pkl

Step 4.Use the link " http://127.0.0.1:8000/api/timeseries/predict/ " in Postman and Select 'POST' method

Step 5.Use the Following input to generate the prediction for next timestamp


[
    {"Temp1": 22.5, "Press1": 1013.2, "Temp2": 23.0, "Press2": 1012.5, "Status": 1},
    {"Temp1": 22.6, "Press1": 1013.3, "Temp2": 23.1, "Press2": 1012.6, "Status": 1},
    {"Temp1": 22.7, "Press1": 1013.4, "Temp2": 23.2, "Press2": 1012.7, "Status": 1},
    {"Temp1": 22.8, "Press1": 1013.5, "Temp2": 23.3, "Press2": 1012.8, "Status": 1},
    {"Temp1": 22.9, "Press1": 1013.6, "Temp2": 23.4, "Press2": 1012.9, "Status": 1},
    {"Temp1": 23.0, "Press1": 1013.7, "Temp2": 23.5, "Press2": 1013.0, "Status": 1},
    {"Temp1": 23.1, "Press1": 1013.8, "Temp2": 23.6, "Press2": 1013.1, "Status": 1},
    {"Temp1": 23.2, "Press1": 1013.9, "Temp2": 23.7, "Press2": 1013.2, "Status": 1},
    {"Temp1": 23.3, "Press1": 1014.0, "Temp2": 23.8, "Press2": 1013.3, "Status": 1},
    {"Temp1": 23.4, "Press1": 1014.1, "Temp2": 23.9, "Press2": 1013.4, "Status": 1}
]
