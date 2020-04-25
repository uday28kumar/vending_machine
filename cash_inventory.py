class CashInventory:
    def __init__(self):
        super().__init__()
        self._cash_inventory = {}

    def add(self, coin_name):
        if(self._has_coin(coin_name)):
            count = self._cash_inventory.get(coin_name)
            self._cash_inventory[coin_name] = count + 1
        else:
            self._cash_inventory[coin_name] = 1

    def _has_coin(self, coin_name):
        if coin_name in self._cash_inventory.keys():
            if self._cash_inventory.get(coin_name) > 0:
                return True

        return False

    def remove(self, coin_name):
        if self._has_coin(coin_name):
            count = self._cash_inventory.get(coin_name)
            self._cash_inventory[coin_name] = count - 1

    def clear(self):
        self._cash_inventory.clear()

    def put(self, coin_name, quantity):
        self._cash_inventory[coin_name] = quantity

    def display(self):
        print(self._cash_inventory)
