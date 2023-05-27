from django.db import models

# Create your models here.

class movie(models.Model):
    rdate = models.DateField()
    movie = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    heroin = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.movie} released at {self.rdate} with rating {self.rating}'