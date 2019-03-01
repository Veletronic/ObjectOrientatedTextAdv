from Room import room
from Item import Item

Kitchen = room("Kitchen")
Kitchen.set_description("The room sparkles and glistens, the surface of the floor reflects your image perfectly...a little too perfectly")


HiddenBasement = room("???")
HiddenBasement.set_description("Darkness has enveloped you. You see nothing but the light bleeding in from where you entered. The air feels differnt here..cold...and oddly hostile.")



Ballroom = room("Ballroom")
Ballroom.set_description("""The door creaks loudly, almost as if it was screaming in agony.
A gust of musty air escapes through the door, pervading your nostrils.
You examine the dimly lit room, nothing but dated leather seats stacked on top of one another and white grungy table cloths are visible..at least at a first glance.""")

Dining = room("Dining room")
Dining.set_description("""A long dining table lays before you, stretched out...almost as if it was greeting you.
It exhibits several platters of what seem to be freshly made food, of which entices you closer.
A slight sour smell exists, but you find it hard to pay any mind to. You're entranced by the display that lays on the table.""")

Kitchen.link_room(Dining, "south")
Kitchen.link_room(HiddenBasement, "west")
Dining.link_room(Kitchen, "north")
Dining.link_room(Ballroom, "west")
Ballroom.link_room(Dining, "east")

DiamondKey = Item("Diamond Key")
DiamondKey.set_itemdescription("""A rusted silver key with a diamond shaped head with a ruby embedded in it.""")

SpadesKey = Item("Spades Key")
SpadesKey.set_itemdescription("""A pristine gold key with a spade shaped head with an emerald embedded in it""")

Pebble = Item("Pebble")
Pebble.set_itemdescription("""A cold and pathetically tiny pebble..what use could you have for this?""")

PillBottle = Item("A pill bottle?")
PillBottle.setitemdescription("""A plain and unlabelled pill bottle.
you shake it and hear some musical rattling, how wonderful.""")






#Dining.get_description() checks linked rooms

current_room = Kitchen          

while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command) 
