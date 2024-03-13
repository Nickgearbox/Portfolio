from django.db import models

class Email(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=200)

    def __str__(self):
        return f'Email from {self.name}'