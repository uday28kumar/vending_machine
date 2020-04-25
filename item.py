class Item:
    def __init__(self):
        super().__init__()
        self._name = ""
        self._price = ""

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def to_string(self):
        return "name: "+str(self._name)+" price: "+str(self._price)
