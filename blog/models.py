from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    slug = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100)
    authorImg = models.ImageField(null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title