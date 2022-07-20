from django.db import models

# Create your models here.
class Health(models.Model):
    Choises = [[(1,'Yes'),(0,'No')], [(1,'1st Dose'),(0,'Fully Vaccinated')]]
    C1, C2 = Choises
    
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True) 
    phonenumber = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    temperature = models.CharField(max_length=20, null=True)
    choise1 = models.BooleanField(null=True, choices=C1)
    travelhistory = models.CharField(max_length=30, null=True)
    choise2 = models.BooleanField(null=True, choices=C2)
    choise3 = models.CharField(max_length=30, null=True)
    img = models.ImageField(upload_to="image/", null=True)
    
    class Meta:
        db_table="HealthForms"