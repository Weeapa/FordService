from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name.capitalize()