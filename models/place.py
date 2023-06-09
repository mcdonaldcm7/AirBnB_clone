#!/usr/bin/python3
"""
This module contains the definition for the 'Place' class which is a subclass
of the 'BaseModel' class
"""


from .base_model import BaseModel


class Place(BaseModel):
    """
    A class representation of a place with several attributes to capture
    information about the plae such as:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be the list
        of Amenity.id later
    """

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
        else:
            for key in kwargs:
                if key == "__class__":
                    continue
                else:
                    setattr(self, key, kwargs[key])
        super().__init__(*args, **kwargs)
