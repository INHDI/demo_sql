from django.db import models

# Create your models here.
class LoginModel(models.Model):
    user = models.CharField(max_length=200, null=True)
    pas = models.CharField(max_length=200, null=True)

class ThemSuaXoa(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
