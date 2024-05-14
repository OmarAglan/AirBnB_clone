#!usr/bin/python3
"""Customise class for the entire project"""

from uuid import uuid4


class BaseModel:
    """Custom Base Model class"""

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel

        Args:
        *args(args): input arguments
        **kwargs(kwargs): input arguments
        """
        if not kwargs:
            self.id = str(uuid4())
