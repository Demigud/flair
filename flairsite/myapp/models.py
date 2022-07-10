from django.db import models

# Create your models here.
class Health(models.Model):
    Choices1 = ( (1,'Yes'),
             (0,'No'),
           )

    Choices2 = ( (1,'1st Dose'),
             (0,'Fully Vaccinated'),
           )

    Choices3 = ( (0,'NONE'), 
             (1,'Headache'),
             (2,'Coughing'),
             (3,'HighFever'),
           )
    
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    phonenumber = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    temperature = models.CharField(max_length=20, null=True)
    choise1 = models.BooleanField(null=True, choices=Choices1)
    choise2 = models.BooleanField(null=True, choices=Choices2)
    choise3 = models.CharField(max_length=2, default='NONE', choices=Choices3)
    
    def _str_(self):
        return self.name