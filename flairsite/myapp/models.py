from django.db import models

# Create your models here.
class HealthForms(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def _str_(self):
        return self.name