class Item:
    def __init__(self):
        super().__init__()
        self._name = ""
        self._price = ""

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def toString(self):
        return "name: "+str(self._name)+" price: "+str(self._price)
