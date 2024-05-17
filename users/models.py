from django.contrib.auth.models import AbstractUser
from django.db import models


class UserConfirmationModel(models.Model):
    code = models.IntegerField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.email} - {self.code}"

    class Meta:
        verbose_name = 'code'
        verbose_name_plural = 'codes'
