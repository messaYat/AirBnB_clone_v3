#!/usr/bin/python3
"""
Place Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey,\
    MetaData, Table, ForeignKey
from sqlalchemy.orm import backref
storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == "db":
    class PlaceAmenity(Base):
        """ PlaceAmenity Class """
        __tablename__ = 'place_amenity'
        metadata = Base.metadata
        id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True)
        place_id = Column(String(60), ForeignKey('places.id'),
                          nullable=False)
        amenity_id = Column(String(60), ForeignKey('amenities.id'),
                            nullable=False)
