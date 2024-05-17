#!/usr/bin/python3
"""This module defines a base class for all models in our HBNB clone"""

import uuid
from models.__init__ import storage
from _datetime import datetime


class BaseModel:
    """A Base Class For All Models"""

    def __init__(self, *args, **kwargs):
        """Start The New Model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
            self.save()

    def __str__(self):
        """Return a String That describes the instance"""
        return '[{}] ({}) {}'.format(BaseModel, self.id, self.__dict__)

    def save(self):
        """Update the Instance's Updated At Attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return A Dictionary Representation of The Instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': BaseModel.__name__})
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary
