from django.db import models

class Register(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    state = models.TextField()
    
    objects = models.Manager()

    def __str__(self):
        return self.description