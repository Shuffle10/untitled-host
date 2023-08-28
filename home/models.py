from django.db import models

# Create your models here.
class Release(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    spotify = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    image = models.ImageField(null=True)


    def __str__(self):
        return self.name



class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self) :
        return self.email

class Quote(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    details = models.TextField()
    

    def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=400)
    artists = models.CharField(max_length=400)
    ticketPrice= models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=400)
    youtube = models.CharField(max_length=400)
    slug = models.CharField(max_length=100, null=True)
    thumbnail_9x16 = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name_first = models.CharField(max_length=400)
    facebook = models.CharField(max_length=400)
    instagram = models.CharField(max_length=400)
    youtube = models.CharField(max_length=400)
    artist_image_wide = models.ImageField(null=True)

    def __str__(self):
        return self.name_first