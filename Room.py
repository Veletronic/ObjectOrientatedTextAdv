import random

class room():
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
    def set_description(self, room_description):
        self.description = room_description
    def get_description(self):
        return self.description
    def get_name(self):
        print ("You are currently in the",self.name)
    def set_name(self,room_name):
        room_name = str(input("Enter room name here: "))
        return room_name
    def describe(self): 
        print( self.description )
    def link_room(self, room_link, direction):
        self.linked_rooms[direction] = room_link
    def get_details(self):
        print( self.name + " linked rooms :" + repr(self.linked_rooms) )
        room.get_name(self)
        room.describe(self)
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print (random.choice(["You storm headfirst into a wall. You may have a mild concussion now..congratulations",
                                  "You faceplant into the wall. You start to wonder what it truly is you're doing with your life",
                                  "One must wonder if it's merely too dark, or if you're truly blind",
                                  "You launch yourself at the wall and hurt yourself in the process. Did you expect a secret passage?",
                                  "As one is destined for greatness, one is also destined for stupidity. You knock your head against the wall"]))
            return self
                   
                                       
                                       
            
            
        
        
