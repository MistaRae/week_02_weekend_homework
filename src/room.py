# define Room class

class Room:
    def __init__(self, name, capacity, cost):
        self.name = name # for referencing appropriate room
        self.capacity = capacity #for check to make sure there is space in the room for 'x' guests or 'n' of guests
        self.cost = cost #cost to hire/entrance cost 
        self.occupants = []  #stores current occupants and checks against capacity to prevent too many people being in a room. 
    
    def check_in(self, guest):
        self.occupants.append(guest)