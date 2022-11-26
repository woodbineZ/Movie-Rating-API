from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    surname = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Directors(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    surname = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField(max_length=400)
    actors = models.ManyToManyField(Actors)
    directors = models.ManyToManyField(Directors)
    premiere = models.DateField()
    updated = models.DateTimeField()
    slug = models.SlugField()

    def number_of_ratings(self):
        return Rating.objects.filter(movie=self).count()
    
    def avg_rating(self):
        score = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            score +=rating.stars
        if len(ratings) > 0:
            return score/len(ratings)
        else:
            return 0

    def __str__(self):
        return f"{self.title}, ({self.premiere})"


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    
    class Meta:
        unique_together=(('user', 'movie'),)
        index_together=(('user', 'movie'),)

    def __str__(self):
        return f"{self.movie.title} Rated by {self.user.username}"

