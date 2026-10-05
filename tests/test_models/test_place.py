#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertIn(type(new.city_id), (str, type(None)))

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertIn(type(new.user_id), (str, type(None)))

    def test_name(self):
        """ """
        new = self.value()
        self.assertIn(type(new.name), (str, type(None)))

    def test_description(self):
        """ """
        new = self.value()
        self.assertIn(type(new.description), (str, type(None)))

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertIn(type(new.number_rooms), (int, type(None)))

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertIn(type(new.number_bathrooms), (int, type(None)))

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertIn(type(new.max_guest), (int, type(None)))

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertIn(type(new.price_by_night), (int, type(None)))

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertIn(type(new.latitude), (float, type(None)))

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertIn(type(new.latitude), (float, type(None)))

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertIn(type(new.amenity_ids), (list, type(None)))
