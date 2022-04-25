from django.db import models

class test(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # representation in django admin
    def __str__(self):
        return self.name + ' ' + self.description