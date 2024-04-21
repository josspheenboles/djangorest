from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    image=models.CharField(max_length=100,null=True)
    latest_version=models.IntegerField(default=1)
    latest_version_date=models.DateTimeField(auto_now=True)
    @classmethod
    def get_list_url(self):
        return reverse('book_list')

