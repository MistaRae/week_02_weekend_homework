import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
import pdb

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.nine_in_nails_fanboy_room = Room("Nine Inch Nails fanboy room", 2, 10)
        self.the_country_room = Room("The Country Room", 1, 10)
        self.mark = Guest("Mark", 33, 100, "Closer")
        self.dan = Guest("Dan", 34, 100, "The Fragile")
        self.sarah = Guest("Sarah", 28, 50, "Drunk like me")
        self.closer = Song("Closer")
        self.the_fragile = Song("The Fragile")
        self.drunk_like_me = Song("Drunk like me")

        #tests for instance variables/format is correct

    def test_room_has_name(self):
        self.assertEqual("Nine Inch Nails fanboy room", self.nine_in_nails_fanboy_room.name)
         
    def test_room_occupants_starts_at_0(self):
        self.assertEqual(0, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_has_capacity(self):
        self.assertEqual(2,self.nine_in_nails_fanboy_room.capacity)

    def test_room_has_cost(self):
        self.assertEqual(10, self.nine_in_nails_fanboy_room.cost)

        #tests for methods

    def test_room_can_check_in(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room,self.mark)
        self.assertEqual(1, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_can_check_out_guests(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room, self.mark)
        self.nine_in_nails_fanboy_room.check_out(self.nine_in_nails_fanboy_room, self.mark)
        self.assertEqual(0, len(self.nine_in_nails_fanboy_room.occupants))

    def test_room_cannot_check_out_guest_thats_not_there(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room,self.mark)
        self.assertEqual("Dan is not in this room, nobody has been checked out.", 
        self.nine_in_nails_fanboy_room.check_out(self.nine_in_nails_fanboy_room,self.dan))

    def test_room_cannot_surpass_capacity_NIN_room(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room,self.mark)
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room,self.dan)
        self.assertEqual("Sorry, this room is at capacity as there are only 2 NIN fanboys allowed",
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room,self.sarah))

    # tests for multiple rooms 

    def test_nonNIN_room_cannot_surpass_capacity(self):
        self.the_country_room.check_in(self.the_country_room,self.sarah)
        self.assertEqual("I'm sorry, this room is at capacity. You can't come in",
        self.the_country_room.check_in(self.the_country_room, self.mark))

    # test adding songs to rooms 

    def test_add_song_to_room(self):
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.closer)
        self.assertEqual(1, len(self.nine_in_nails_fanboy_room.tracklist))

    def test_whats_playing(self):
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.closer)
        self.assertEqual("Closer", self.nine_in_nails_fanboy_room.tracklist[-1].name)

    def test_whats_playing_with_larger_tracklist(self):
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.closer)
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.the_fragile)
        self.assertEqual("The Fragile", self.nine_in_nails_fanboy_room.tracklist[-1].name)

    def test_people_react_to_favourite_song_playing(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room, self.mark)
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room, self.dan)
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.closer)
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.the_fragile)
        self.assertEqual("Dan: WHOOP!", self.nine_in_nails_fanboy_room.favourite_song_playing(self.nine_in_nails_fanboy_room))

    def test_display_tracklist(self):
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room, self.mark)
        self.nine_in_nails_fanboy_room.check_in(self.nine_in_nails_fanboy_room, self.dan)
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.closer)
        self.nine_in_nails_fanboy_room.add_song(self.nine_in_nails_fanboy_room, self.the_fragile)
        self.assertEqual(["Closer", "The Fragile"],
            self.nine_in_nails_fanboy_room.display_tracklist(self.nine_in_nails_fanboy_room) )