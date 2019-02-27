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
        print( self.name + " linked rooms :" + repr(self.linked_rooms) )
