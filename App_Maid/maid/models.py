from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to='media')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)


class maid(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to='media')
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    detail = models.CharField(max_length=255)
    skill = models.CharField(max_length=255)
    review = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class statusmaid(models.Model):
    maid_name = models.ForeignKey(maid, on_delete=models.CASCADE)
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return "{}".format(self.maid.name)


class historymaid(models.Model):
    maid_history = models.ForeignKey(maid, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.maid.name)
