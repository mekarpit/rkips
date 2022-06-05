from django.db import models

# Create your models here.
class RKIPSLI(models.Model):
    RegNo = models.IntegerField
    Name = models.CharField(max_length=15)
    Grade = models.CharField(max_length=15)
    
    

    def __str__(self):
        return self.Name