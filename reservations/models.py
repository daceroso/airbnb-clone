from django.db import models
from core import models as core_models
# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservation Model Definition """

