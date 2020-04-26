class CashInventory:
    def __init__(self):
        super().__init__()
        self._cashInventory = {"penny": 0,
                               "nickel": 0, "dime": 0, "quarter": 0}

    def add(self, coinName):
        if(self.hasCoin(coinName)):
            count = self._cashInventory.get(coinName)
            self._cashInventory[coinName] = count + 1
        else:
            self._cashInventory[coinName] = 1

    def addBulk(self, coinName, quantity):
        self._cashInventory[coinName] = self._cashInventory.get(
            coinName)+quantity

    def hasCoin(self, coinName):
        if coinName in self._cashInventory.keys():
            if self._cashInventory.get(coinName) > 0:
                return True

        return False

    def remove(self, coinName):
        if self.hasCoin(coinName):
            count = self._cashInventory.get(coinName)
            self._cashInventory[coinName] = count - 1

    def clear(self):
        self._cashInventory.clear()

    def put(self, coinName, quantity):
        self._cashInventory[coinName] = quantity

    def display(self):
        print(self._cashInventory)
