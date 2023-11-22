from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    madeIn = models.CharField(max_length=200)
    characteristic = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)