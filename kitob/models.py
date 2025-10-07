from django.db import models

# Create your models here.


class Author(models.Model):
    ism = models.CharField(max_length=100)
    tugilgan_yil = models.IntegerField()

    def __str__(self):
        return self.ism
    
    
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=45)
    yil = models.IntegerField(null=True,blank=True)
          