from django.db import models

# Create your models here.
class deploy_data(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(default="example@gmail.com")
    mobile=models.IntegerField(unique=True)
