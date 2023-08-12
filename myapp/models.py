from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    status_choices=[
        ('pending','pending'),
        ('completed','completed')
    ]
    priority_choices=[
        ("low","low"),
        ("medium","medium"),
        ("high","high")
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20,choices=status_choices)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date  = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20,choices=priority_choices)



