#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    if storage_type == "db":
        reviews = relationship("Review", cascade="all,delete", backref="place")
    else:
        @property
        def reviews(self):
            """reviews getter"""
            from models import storage
            amenity_list = []
            amenity_all = storage.all(Amenity)
            for a in amenity_all.values():
                if a.place_id == self.id:
                    amenity_list.append(a)
            return amenity_list
