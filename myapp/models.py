from django.db import models

# Create your models here.
class Health(models.Model):
    Choises = [(1,'Yes'),(0,'No')]
    C1 = Choises
    
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True) 
    phonenumber = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    temperature = models.CharField(max_length=20, null=True)
    choise1 = models.BooleanField(null=True, choices=C1)
    travelhistory = models.CharField(max_length=30, null=True)
    choise2 = models.ImageField(upload_to="vax_cards", null=True)
    choise3 = models.CharField(max_length=30, null=True)
    img = models.ImageField(upload_to="student_img", null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
