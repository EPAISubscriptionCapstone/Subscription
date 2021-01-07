import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Subscriber(models.Model):
    firstname = models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    #sub_unsub_date = models.DateTimeField('date subscribed or unsubscribed')

    def __str__(self):
        return self.firstname

    #def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

