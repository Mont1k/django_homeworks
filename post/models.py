from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    madeIn = models.CharField(max_length=200)
    characteristic = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category')

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Review(models.Model):
    product = models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
