class Item:
    def __init__(self, item):
        self.item = item
        self.description = None
        self.activate = None
        self.inventory = {}
    def set_description(self, description):
        self.description = description
    def get_description(self):
        print (self.description)
    def set_itemName(self, itemname):
        self.item = itemname
    def get_itemname(self):
        print (self.item)
    def describe(self):
        Item.get_description(self)
        Item.get_itemname(self)

        
        

            
            
        
    
        
