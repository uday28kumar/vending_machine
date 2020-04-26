class Coin:
    def __init__(self):
        super().__init__()
        self._name = ""
        self._value = ""

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getValue(self):
        return self._value

    def setValue(self, price):
        self._value = price

    def toString(self):
        return "name: "+str(self._name)+" value: "+str(self._value)
