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
