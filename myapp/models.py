from django.db import models

# Create your models here.

class Covid(models.Model):
    gender = models.IntegerField()
    age = models.IntegerField()
    diabetes = models.IntegerField()
    asthma = models.IntegerField()
    hypertension = models.IntegerField()
    obesity = models.IntegerField()
    icu = models.IntegerField()
    prediction_result = models.BooleanField(default=False)
    # classification = models.IntegerField()
    
    def __int__(self):
        return self.age

class CovidPredict(models.Model):
    cough = models.IntegerField()
    fever = models.IntegerField()
    sore_throat = models.IntegerField()
    shortness_of_breath = models.IntegerField()
    head_ache = models.IntegerField()
    classification = models.IntegerField()
    
    def __int__(self):
        return self.cough