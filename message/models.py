from django.db import models

class query(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Subject=models.CharField(max_length=50)
    Contact=models.CharField(max_length=20)
    Message=models.TextField()
    
    def __str__(self):
        return self.Name
# Create your models here.
