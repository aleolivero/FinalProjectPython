from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Players(models.Model):

    #user = models.OneToOneField(User,blank=False,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    date_birth = models.DateField(blank=True,null=True, verbose_name="Birth",)
    phone = models.CharField(max_length=100, verbose_name="Phone")
    adress = models.CharField(max_length=100, verbose_name="Adress")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    country = models.CharField(max_length=100, verbose_name="Country")

    def __str__(self,):
        return str(self.first_name) + ' ' + str(self.last_name)
    
class Questions(models.Model):

    title = models.CharField(max_length=1000, verbose_name="Title")
    subtitle = models.CharField(max_length=1000, verbose_name="Sub Title")
    question = models.CharField(max_length=1000, verbose_name="Question")
    image = models.ImageField(verbose_name="Image")
    data = models.DateField(verbose_name="Date")
    correct_answer = models.CharField(max_length=1000, verbose_name="Correct Answer")
    author = models.ForeignKey(Players,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Player")

    def __str__(self,):
        return str(self.question)


class Answers(models.Model):

    answer = models.CharField(max_length=1000, verbose_name="Answer")
    player = models.ForeignKey(Players,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Player")
    question = models.ForeignKey(Questions,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Question")

    def __str__(self,):
        return str(self.answer)