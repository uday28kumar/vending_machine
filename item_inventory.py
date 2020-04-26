class ItemInventory:
    def __init__(self):
        super().__init__()
        self._itemInventory = {"coke": 0, "pepsi": 0, "soda": 0}

    def add(self, itemName):
        if(self.hasItem(itemName)):
            count = self._itemInventory.get(itemName)
            self._itemInventory[itemName] = count + 1
        else:
            self._itemInventory[itemName] = 1

    def hasItem(self, itemName):
        if itemName in self._itemInventory.keys():
            if self._itemInventory.get(itemName) > 0:
                return True

        return False

    def remove(self, itemName):
        if self.hasItem(itemName):
            count = self._itemInventory.get(itemName)
            self._itemInventory[itemName] = count - 1

    def clear(self):
        self._itemInventory.clear()

    def put(self, itemName, quantity):
        self._itemInventory[itemName] = quantity

    def display(self):
        print(self._itemInventory)
