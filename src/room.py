# define Room class

class Room:
    def __init__(self, name, capacity, cost):
        self.name = name # for referencing appropriate room
        self.capacity = capacity #for check to make sure there is space in the room for 'x' guests or 'n' of guests
        self.cost = cost #cost to hire/entrance cost 
        self.occupants = []  #stores current occupants and checks against capacity to prevent too many people being in a room. 
    
    #room has capacity so the room controls check-in and and check-out
    def check_in(self, room, guest):
        if room.name == "Nine Inch Nails fanboy room":
            if len(room.occupants) < room.capacity:
                self.occupants.append(guest)
            return "Sorry, this room is at capacity as there are only 2 NIN fanboys allowed"
        if len(self.occupants) < self.capacity:
                    self.occupants.append(guest)
        return "I'm sorry, this room is at capacity. You can't come in"

    def check_out(self, room, guest):
        
        if guest in room.occupants:
            self.occupants.remove(guest)
        return f"{guest.name} is not in this room, nobody has been checked out."