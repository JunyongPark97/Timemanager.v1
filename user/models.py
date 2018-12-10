from datetime import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
import user


class User(AbstractUser):
    grade= models.IntegerField()
    writter_id=models.CharField(null=True,max_length=10)


class Timelog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    keyword=models.IntegerField(choices=((1,'출근'),(2,'퇴근'), (3, '출근 (재택)'), (4, '퇴근 (재택)')))
    created_at=models.DateTimeField()
    text = models.CharField(max_length=10)
    half_day_off=models.CharField(blank=True,null=True,max_length=10)#반차 기록
    breaktime = models.IntegerField(default=0)


class RequestInfo(models.Model):
    sender=models.ForeignKey(User, related_name='senderRequestinfo',on_delete=models.CASCADE)
    receiver=models.ForeignKey(User, related_name='receiverRequestinfo',on_delete=models.CASCADE)
    timelog=models.ForeignKey(Timelog, on_delete=models.CASCADE)
    update=models.DateTimeField()
    breaktime=models.IntegerField(default=0)
    status = models.IntegerField(default=0, choices=((0,'대기중'),(1,'수락'),(2,'거절')))
    reason=models.TextField(null=True)

class Timeinfo(models.Model):
    timelog=models.ForeignKey(Timelog, on_delete=models.CASCADE)
