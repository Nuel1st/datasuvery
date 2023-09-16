from django.db import models

class Waypoint(models.Model):
    chainage = models.IntegerField()
    location = models.TextField()  # You can use a TextField to store map coordinates
    photo = models.ImageField(upload_to='waypoint_photos/')

    class Meta:
        abstract = True  # This makes the Waypoint model abstract to reuse its fields

class StartPoint(Waypoint):
    pass

class EndPoint(Waypoint):
    pass
