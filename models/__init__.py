#!/usr/bin/python3
"""This module instantiates the storage engine selected by
the HBNB_TYPE_STORAGE environment variable (file by default)"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

from models.base_model import BaseModel  # noqa: E402
from models.user import User  # noqa: E402
from models.state import State  # noqa: E402
from models.city import City  # noqa: E402
from models.amenity import Amenity  # noqa: E402
from models.place import Place  # noqa: E402
from models.review import Review  # noqa: E402
