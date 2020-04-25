from item import Item
from coin import Coin
from bucket import Bucket
from item_inventory import ItemInventory
from cash_inventory import CashInventory


coin_value = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}

item_price = {"coke": 25, "pepsi": 35, "soda": 45}


class VendingMachine:
    def __init__(self):
        super().__init__()
        self._cash_inventory = CashInventory()
        self._item_inventory = ItemInventory()
        self._total_sales = 0
        self._current_item = None
        self._current_balance = 0
        self._initilize_item_inventory()
        self._initilize_cash_inventory()

    def _initilize_item_inventory(self):
        """initilize item inventory by 5 items of each type"""
        for item_name in item_price.keys():
            for j in range(5):
                self._item_inventory.add(item_name)

    def _initilize_cash_inventory(self):
        """initilize cash inventory by 5 coins of each type"""
        for coin_name in coin_value.keys():
            for j in range(5):
                self._cash_inventory.add(coin_name)

    def display_stats(self):
        """display the current stat of machine"""
        print("Items: available number: ", flush=True)
        self._item_inventory.display()
        print("Coin: available number: ", flush=True)
        self._cash_inventory.display()

    def reset(self):
        """reset the vending machine"""
        self._cash_inventory.clear()
        self._item_inventory.clear()
        self._total_sales = 0
        self._current_item = None
        self._current_balance = 0

    def get_current_balance(self):
        """return current balance inserted"""
        return self._current_balance

    def select_item_and_get_price(self, item_name):
        """return price of input item"""
        if self._item_inventory._has_item(item_name):
            self._current_item = Item()
            self._current_item.set_name(item_name)
            self._current_item.set_price(item_price.get(item_name))
            return self._current_item.get_price()
        print("Item sold out! Please try other item.")
        return -1

    def insert_coin(self, coin_name):
        """insert coins and calculate current balance"""
        value = coin_value.get(coin_name)
        self._current_balance = self._current_balance + value
        self._cash_inventory.add(coin_name)

    def _get_change(self, amount):
        """return change of input amount"""
        changes = []
        if amount > 0:
            balance = amount
            while balance > 0:
                if balance >= coin_value.get("quarter") and self._cash_inventory._has_coin("quarter"):
                    balance = balance - coin_value.get("quarter")
                    change_coin = Coin()
                    change_coin.set_name("quarter")
                    change_coin.set_value(coin_value.get("quarter"))
                    changes.append(change_coin)
                    continue

                elif balance >= coin_value.get("dime") and self._cash_inventory._has_coin("dime"):
                    balance = balance - coin_value.get("dime")
                    change_coin = Coin()
                    change_coin.set_name("dime")
                    change_coin.set_value(coin_value.get("dime"))
                    changes.append(change_coin)
                    continue

                elif balance >= coin_value.get("nickel") and self._cash_inventory._has_coin("nickel"):
                    balance = balance - coin_value.get("nickel")
                    change_coin = Coin()
                    change_coin.set_name("nickel")
                    change_coin.set_value(coin_value.get("nickel"))
                    changes.append(change_coin)
                    continue

                elif balance >= coin_value.get("penny") and self._cash_inventory._has_coin("penny"):
                    balance = balance-coin_value.get("penny")
                    change_coin = Coin()
                    change_coin.set_name("penny")
                    change_coin.set_value(coin_value.get("penny"))
                    changes.append(change_coin)
                    continue
                else:
                    print("Sorry I don't have sufficient change!!", flush=True)
                    return [None]

        return changes

    def _is_fully_paid(self):
        """check the amount is fully paid or not"""
        if self._current_balance >= self._current_item.get_price():
            return True
        return False

    def _has_sufficent_change_for_amount(self, amount):
        """check whether the machine has sufficient change or not"""
        if len(self._get_change(amount)) == 0:
            return True
        if self._get_change(amount)[0] == None:
            return False
        return True

    def _has_sufficent_change(self):
        """return false if machine has sufficent change otherwise return false"""
        return self._has_sufficent_change_for_amount(self._current_balance - self._current_item.get_price())

    def _collect_item(self):
        """buy item from machine"""
        if self._is_fully_paid():
            if self._has_sufficent_change():
                self._item_inventory.remove(self._current_item.get_name())
                return self._current_item
            else:
                print(
                    "Sorry! Sufficient change is not available in machine!", flush=True)
                self._current_item.set_name(None)
                self._current_item.set_price(0)
                return self._current_item

        remaining_balance = self._current_item.get_price() - self._current_balance
        print("Price is not fully paid, Remaining: " +
              str(remaining_balance), flush=True)
        self._current_item.set_name(None)
        self._current_item.set_price(0)
        return self._current_item

    def _update_cash_inventory(self, change):
        """update cash in cash inventory"""
        for coin in change:
            self._cash_inventory.remove(coin.get_name())

    def get_total_sales(self):
        """return total sales amount"""
        return self._total_sales

    def _collect_change(self):
        """collect change after buy"""
        change_amount = self._current_balance - self._current_item.get_price()
        change = self._get_change(change_amount)
        self._update_cash_inventory(change)
        self._current_balance = 0
        self._current_item = None
        return change

    def collect_item_and_change(self):
        """collect item and change after buy in bucket"""
        bought_item = self._collect_item()
        self._total_sales = self._total_sales + self._current_item.get_price()
        returned_changes = self._collect_change()
        bucket = Bucket()
        bucket.set_item(bought_item)
        bucket.set_changes(returned_changes)
        return bucket

    def display_bucket(self, bucket):
        """print bucket value"""
        print("Item: "+str(bucket.get_item().get_name()))
        print("Change: ", end='')
        for change in bucket.get_changes():
            print(str(change.get_name()) +
                  "(value = "+str(change.get_value())+"), ", end='')
        print("", flush=True)


if __name__ == "__main__":
    vendingMachine = VendingMachine()

    print("\n********** Menu *****************")
    print("Item and their price: ")
    print(item_price)
    print("Coins and their value")
    print(coin_value)
    print("**********************************\n")
    while True:
        print("\n1. Display Vending Machine stat.")
        print("2. Select item and buy.")
        print("3. Total sales amount.")
        print("4. Reset Machine.")

        print("0. Exit", flush=True)
        choice = input("Enter choice: ")
        if choice == '1':
            vendingMachine.display_stats()
        elif choice == '2':
            item_name = input("Enter item name: ")
            item_price = vendingMachine.select_item_and_get_price(
                item_name.lower())
            if(item_price == -1):
                continue

            print("Item: "+item_name.lower() +
                  " | Price: "+str(item_price), flush=True)
            buy = input("Want to buy (y/n): ")
            if buy == 'y' or buy == 'Y':
                while item_price > vendingMachine.get_current_balance():
                    inserted_coin = input(
                        "Please insert coin-name (one at a time) || (n) to terminate: ")
                    if(inserted_coin == 'n'):
                        break
                    if inserted_coin.lower() not in coin_value.keys():
                        print("invalid input!", flush=True)
                        break

                    vendingMachine.insert_coin(inserted_coin.lower())

                bucket = vendingMachine.collect_item_and_change()
                print("\nPlease collect your item and change: ")
                vendingMachine.display_bucket(bucket)
        elif choice == '3':
            print(vendingMachine.get_total_sales(), flush=True)
        elif choice == '4':
            vendingMachine.reset()
        else:
            exit()
