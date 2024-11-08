from django.db import models

class cars(models.Model):
    cars_name = models.CharField(max_length=250)
    cars_colour = models.CharField(max_length=250)
    cars_price = models.IntegerField()
    cars_models = models.CharField(max_length=250)
    

    def __str__(self):
        return self.cars_name
