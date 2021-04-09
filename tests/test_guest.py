import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.mark = Guest("Mark", 33, 100, "Closer")

    def test_guest_has_name(self):
        self.assertEqual("Mark", self.mark.name)

    def test_guest_has_age(self):
        self.assertEqual(33, self.mark.age)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.mark.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Closer", self.mark.fav_song)
