from django.db import models

class Genre(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="Non Name")

class Music(models.Model) :
    id = models.AutoField(primary_key=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100, default="Non Title")
    singer = models.CharField(max_length=20, default="Various")
    year = models.IntegerField(default=1900)