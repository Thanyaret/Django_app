from django.db import models

# Create your models here.
class User(models.Model):
    photo = models.ImageField(blank=True,null=True,upload_to='media')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class maid(models.Model):
    photo = models.ImageField(blank=True,null=True,upload_to='media')
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    detail = models.CharField(max_length=255)
    date = models.DateTimeField()
    skill = models.CharField(max_length=255)
    review = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)

class statusmaid(models.Model):
    maid = models.ForeignKey(maid,on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return "{}".format(self.maid.name)

class historymaid(models.Model):
    maid = models.ForeignKey(maid,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.maid.name)