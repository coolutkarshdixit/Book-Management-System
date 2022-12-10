from django.db import models

# Create your models here.
class ContactZ (models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name+" , "+self.email
    
class BookM(models.Model):
    sn=models.AutoField(primary_key=True)
    bid=models.CharField(max_length=100,unique=True)
    bname=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    bcat=models.CharField(max_length=100)
    def __str__(self):
        return self.bname+","+self.bcat+","+self.author