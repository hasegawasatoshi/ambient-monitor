from django.core import validators
from django.db import models


class Sensor(models.Model):
    id = models.CharField(
        verbose_name="S/N",
        primary_key=True,
        max_length=64,
        blank=False,
        null=False,
        validators=[validators.RegexValidator(
            regex='^[0-9a-zA-Z-]+$',
            message='numeric, alphabet or hylien'
        )])
    label = models.CharField(
        verbose_name="Label",
        max_length=128,
        blank=True,
        null=False)
    owner = models.ForeignKey(
        'auth.User',
        related_name='sensor',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
