from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=120)
    answer = models.CharField(max_length=600)


class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    isAvailable=models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consultant=models.ForeignKey(Consultant, on_delete=models.CASCADE)
    isEnded = models.BooleanField(default=False)


class Message(models.Model):
    conversation=models.ForeignKey(Conversation, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=120)