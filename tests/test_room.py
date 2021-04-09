import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.nine_in_nails_fanboy_room = Room("Nine Inch Nails fanboy room", 2, 10)
        self.mark = Guest("Mark", 33, 100, "Closer")
        self.dan = Guest("Dan", 34, 100, "The Fragile" )

    def test_room_has_name(self):
        self.assertEqual("Nine Inch Nails fanboy room", self.nine_in_nails_fanboy_room.name)
         
    def test_room_occupants_starts_at_0(self):
        self.assertEqual(0, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_has_capacity(self):
        self.assertEqual(2,self.nine_in_nails_fanboy_room.capacity)

    def test_room_has_cost(self):
        self.assertEqual(10, self.nine_in_nails_fanboy_room.cost)

    def test_room_can_check_in(self):
        self.nine_in_nails_fanboy_room.check_in(self.mark)
        self.assertEqual(1, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_can_check_out_guests(self):
        self.nine_in_nails_fanboy_room.check_in(self.mark)
        self.nine_in_nails_fanboy_room.check_out(self.mark)
        self.assertEqual(0, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_cannot_check_out_guest_thats_not_there(self):
        self.nine_in_nails_fanboy_room.check_in(self.mark)
        self.assertEqual("Dan is not in this room, nobody has been checked out.", self.nine_in_nails_fanboy_room.check_out(self.dan))