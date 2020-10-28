from django.db import models
from core import models as core_models
from rooms.models import Room
from users.models import User


class Review(core_models.TimeStampedModel):
    """  Review Model Definition """
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    values = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room.name}'
