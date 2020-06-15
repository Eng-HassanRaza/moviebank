from django.db import models
from jsonfield import JSONField

class Movies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    imgPath = models.ImageField()
    duration = models.IntegerField()
    genre = JSONField()
    language = models.CharField(max_length=30)
    mpaaRating = JSONField()
    userRating = models.CharField(max_length=30)

    class Meta:
        db_table = "movies"

    def __str__(self):
        return self.name