#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timedelta
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
TIME_FMT = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id (sqlalchemy String): primary key, a uuid4 string
        created_at (sqlalchemy DateTime): creation datetime
        updated_at (sqlalchemy DateTime): last update datetime
    """
    id = Column(String(60), nullable=False, primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if self.updated_at <= self.created_at:
                self.updated_at = self.created_at + timedelta(microseconds=1)
            if getenv("HBNB_TYPE_STORAGE") != "db":
                from models import storage
                storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at') and \
                        isinstance(value, str):
                    value = datetime.strptime(value, TIME_FMT)
                setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if isinstance(dictionary.get('created_at'), datetime):
            dictionary['created_at'] = dictionary['created_at'].isoformat()
        if isinstance(dictionary.get('updated_at'), datetime):
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
