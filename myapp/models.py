from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return '%s %s' % (self.user, self.album_name)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return '%s %s' %(self.album, self.image)
