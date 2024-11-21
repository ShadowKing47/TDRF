from django.db import models
# Create your models here.


class PredictionInput(models.Model):
    Temp1 = models.FloatField()  # Temperature 1
    Press1 = models.FloatField()  # Pressure 1
    Temp2 = models.FloatField()  # Temperature 2
    Press2 = models.FloatField()  # Pressure 2
    Status = models.FloatField()  # Status value (which could be either a float or int)

    def __str__(self):
        return f"Temp1: {self.Temp1}, Press1: {self.Press1}, Temp2: {self.Temp2}, Press2: {self.Press2}, Status: {self.Status}"
