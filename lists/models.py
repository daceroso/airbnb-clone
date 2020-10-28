from django.db import models

from rooms import models as rooms_models
from users import models as users_models
from core import models as core_models


# Create your models here.


class List(core_models.TimeStampedModel):
    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(rooms_models.Room, blank=True)

    def __str__(self):
        return self.name
