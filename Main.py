from Room import room

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
Ballroom.linkroom(
