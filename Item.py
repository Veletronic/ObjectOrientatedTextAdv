class Item:
    def __init__(self, item):
        self.item = None
        self.description = None
        self.activate = None
        self.exists = {}
    def SetDescription(self, description):
        self.description = description
    def GetDescription(self):
        return self.description
    def SetItemName(self, itemname):
        self.item = itemname
    def GetItemName(self):
        print self.item
    def describe(self):
        GetDescription(self)
        GetItemName(self)
    def find(self, examine):
    
        
