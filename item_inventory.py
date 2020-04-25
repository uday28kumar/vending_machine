class ItemInventory:
    def __init__(self):
        super().__init__()
        self._item_inventory = {}

    def add(self, item_name):
        if(self._has_item(item_name)):
            count = self._item_inventory.get(item_name)
            self._item_inventory[item_name] = count + 1
        else:
            self._item_inventory[item_name] = 1

    def _has_item(self, item_name):
        if item_name in self._item_inventory.keys():
            return True
        return False

    def remove(self, item_name):
        if self._has_item(item_name):
            count = self._item_inventory.get(item_name)
            self._item_inventory[item_name] = count - 1

    def clear(self):
        self._item_inventory.clear()

    def put(self, item_name, quantity):
        self._item_inventory[item_name] = quantity

    def display(self):
        print(self._item_inventory)
