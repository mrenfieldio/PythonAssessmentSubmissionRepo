from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.TextField(null=True)
    stars = models.IntegerField()
    forks = models.IntegerField()

    def __str__(self):
        return self.name
