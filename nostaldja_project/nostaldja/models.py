from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=30)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Fad(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self) -> str:
        return self.name

