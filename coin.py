class Coin:
    def __init__(self):
        super().__init__()
        self._name = ""
        self._value = ""

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_value(self):
        return self._value

    def set_value(self, price):
        self._value = price

    def to_string(self):
        return "name: "+str(self._name)+" value: "+str(self._value)
