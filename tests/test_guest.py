import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestGuest(unittest.TestCase):

    #testing instance variables line up as expected 

    def setUp(self):
        self.mark = Guest("Mark", 33, 100, "Closer")
        self.nine_in_nails_fanboy_room = Room("Nine Inch Nails fanboy room", 2, 10)

    def test_guest_has_name(self):
        self.assertEqual("Mark", self.mark.name)

    def test_guest_has_age(self):
        self.assertEqual(33, self.mark.age)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.mark.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Closer", self.mark.fav_song)

    #testing for methods

    def test_guest_can_pay_an_entry_fee(self):
        self.mark.pay_entry(self.mark, self.nine_in_nails_fanboy_room)
        self.assertEqual(90, self.mark.wallet)