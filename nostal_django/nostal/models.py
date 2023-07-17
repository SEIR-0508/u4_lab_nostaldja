from django.db import models

class Decades (models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class Fads (models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=100)
    decade = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.decade

    


# Create your models here.
