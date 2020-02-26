from django.db import models

# Create your models here.

class Question(models.Model):

    no = models.AutoField(primary_key=True)
    question = models.TextField()
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    set = models.IntegerField()

    def __str__(self):

        return self.question

class Result(models.Model):

    registration_no =  models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=100)
    stamp = models.DateTimeField(auto_now_add=True)
    score = models.CharField(max_length=100)
    score2 = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.registration_no
    