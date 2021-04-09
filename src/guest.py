#define Guest class

class Guest:
    def __init__(self, name, age, wallet, fav_song):
        self.name = name #for referencing appropriate person
        self.age = age #for age check to buy alcohol
        self.wallet = wallet #for funds check to make sure they can rent a room/buy alcohol
        self.fav_song = fav_song # for checking song being played in room 

    def pay_entry(self, guest, room):
        guest.wallet -= room.cost