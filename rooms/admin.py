from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class RoomAdmin(admin.ModelAdmin):
    """ Item Admin Definition """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    list_display = ('name',
                    'country',
                    'city',
                    'price',
                    'guests',
                    'beds',
                    'bedrooms',
                    'baths',
                    'check_in',
                    'check_out',
                    'instant_book',
                    )
    list_filter = ('instant_book', 'city', 'country')


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """  """
    pass
