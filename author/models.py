from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bdate = models.DateField()
    image = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name
