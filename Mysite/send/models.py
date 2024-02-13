import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser
# Create your models here.





class messages(models.Model):
    text = models.TextField(null=False,blank=False)
    written_by = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
    def __str__(self):
        return self.text
