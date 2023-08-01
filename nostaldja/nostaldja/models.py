from django.db import models

# Create your models here.
class Decades(models.Model):
    name = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField() 


    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField(max_length=200, null=True)
    description = models.CharField(max_length=100)
    decade = models.ForeignKey(Decades, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 