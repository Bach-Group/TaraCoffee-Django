from django.db import models


class Menu(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(null=True, default=0)
    image=models.ImageField(upload_to='project/image/imageproduct/')

    def __str__(self):
        return self.name

class Config(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return self.code


class Imageslider(models.Model):
    code=models.CharField(max_length=30)
    image=models.ImageField(upload_to='project/image/imageslider/')

    def __str__(self):
        return self.code




# Create your models here.
