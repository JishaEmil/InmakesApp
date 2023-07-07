from django.db import models

# Create your models here.
class games(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
#to show added table rows in admin panel with name
    def __str__(self):
      return self.name
