from item import Item
from coin import Coin
from bucket import Bucket
from item_inventory import ItemInventory
from cash_inventory import CashInventory


coinValue = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}

itemPrice = {"coke": 25, "pepsi": 35, "soda": 45}


class VendingMachine:
    def __init__(self):
        super().__init__()
        self._cashInventory = CashInventory()
        self._itemInventory = ItemInventory()
        self._totalSales = 0
        self._currentItem = None
        self._currentBalance = 0
        self._currentlyInsertedCoins = []
        self._initilizeItemInventory()
        self._initilizeCashInventory()

    def _initilizeItemInventory(self):
        """initilize item inventory by 5 items of each type"""
        for itemName in itemPrice.keys():
            for j in range(5):
                self._itemInventory.add(itemName)

    def _initilizeCashInventory(self):
        """initilize cash inventory by 5 coins of each type"""
        for coinName in coinValue.keys():
            for j in range(5):
                self._cashInventory.add(coinName)

    def _refund(self):
        """refund change if change not available"""
        refund = self._currentlyInsertedCoins
        self._updateCashInventory(refund)
        return refund

    def _collectChange(self):
        """collect change after buy"""
        changeAmount = self._currentBalance - self._currentItem.getPrice()
        change = self._getChange(changeAmount)
        self._updateCashInventory(change)
        return change

    def _getChange(self, amount):
        """return change of input amount"""
        changes = []
        if amount > 0:
            balance = amount
            currentlyDeducted = {"penny": 0,
                                 "nickel": 0, "dime": 0, "quarter": 0}
            while balance > 0:
                change_coin = Coin()
                if balance >= coinValue.get("quarter") and self._cashInventory.hasCoin("quarter"):
                    balance = balance - coinValue.get("quarter")
                    change_coin.setName("quarter")
                    change_coin.setValue(coinValue.get("quarter"))
                    changes.append(change_coin)
                    self._cashInventory.remove("quarter")
                    currentlyDeducted["quarter"] = currentlyDeducted.get(
                        "quarter")+1
                    continue
                elif balance >= coinValue.get("dime") and self._cashInventory.hasCoin("dime"):
                    balance = balance - coinValue.get("dime")
                    change_coin.setName("dime")
                    change_coin.setValue(coinValue.get("dime"))
                    changes.append(change_coin)
                    self._cashInventory.remove("dime")
                    currentlyDeducted["dime"] = currentlyDeducted.get(
                        "dime")+1
                    continue
                elif balance >= coinValue.get("nickel") and self._cashInventory.hasCoin("nickel"):
                    balance = balance - coinValue.get("nickel")
                    change_coin.setName("nickel")
                    change_coin.setValue(coinValue.get("nickel"))
                    changes.append(change_coin)
                    self._cashInventory.remove("nickel")
                    currentlyDeducted["nickel"] = currentlyDeducted.get(
                        "nickel")+1
                    continue
                elif balance >= coinValue.get("penny") and self._cashInventory.hasCoin("penny"):
                    balance = balance - coinValue.get("penny")
                    change_coin.setName("penny")
                    change_coin.setValue(coinValue.get("penny"))
                    changes.append(change_coin)
                    self._cashInventory.remove("penny")
                    currentlyDeducted["penny"] = currentlyDeducted.get(
                        "penny")+1
                    continue
                else:
                    return [None]

            for coinName in currentlyDeducted.keys():
                self._cashInventory.addBulk(
                    coinName, currentlyDeducted.get(coinName))

        return changes

    def _isFullyPaid(self):
        """check the amount is fully paid or not"""
        if self._currentBalance >= self._currentItem.getPrice():
            return True
        return False

    def _hasSufficentChangeForAmount(self, amount):
        """check whether the machine has sufficient change or not"""
        withChange = self._getChange(amount)
        if len(withChange) == 0:
            return True
        if withChange[0] == None:
            return False
        return True

    def _hasSufficentChange(self):
        """return false if machine has sufficent change otherwise return false"""
        return self._hasSufficentChangeForAmount(self._currentBalance - self._currentItem.getPrice())

    def _collectItem(self):
        """buy item from machine"""
        if self._isFullyPaid():
            if self._hasSufficentChange():
                self._itemInventory.remove(self._currentItem.getName())
                return True
            else:
                print(
                    "Sorry! Sufficient change is not available in machine!", flush=True)
                return False

        remaining_balance = self._currentItem.getPrice() - self._currentBalance
        print("Price is not fully paid, Remaining: " +
              str(remaining_balance), flush=True)
        return False

    def _updateCashInventory(self, change):
        """update cash in cash inventory"""
        for coin in change:
            self._cashInventory.remove(coin.getName())

    def reset(self):
        """reset the vending machine"""
        self._cashInventory = CashInventory()
        self._itemInventory = ItemInventory()
        self._totalSales = 0
        self._currentItem = None
        self._currentBalance = 0

    def putItem(self, inputItem, quantity):
        self._itemInventory.put(inputItem, int(quantity))

    def putCoin(self, inputCoin, quantity):
        self._cashInventory.put(inputCoin, int(quantity))

    def displayStats(self):
        """display the current stat of machine"""
        print("Items: available number: ", flush=True)
        self._itemInventory.display()
        print("Coin: available number: ", flush=True)
        self._cashInventory.display()

    def getCurrentBalance(self):
        """return current balance inserted"""
        return self._currentBalance

    def selectItemAndGetPrice(self, itemName):
        """return price of input item"""
        if self._itemInventory.hasItem(itemName):
            self._currentItem = Item()
            self._currentItem.setName(itemName)
            self._currentItem.setPrice(itemPrice.get(itemName))
            return self._currentItem.getPrice()
        print("Item sold out! Please try other item.")
        return -1

    def insertCoin(self, coinName):
        """insert coins and calculate current balance"""
        value = coinValue.get(coinName)
        i_coin = Coin()
        i_coin.setName(coinName)
        i_coin.setValue(value)
        self._currentlyInsertedCoins.append(i_coin)
        self._currentBalance = self._currentBalance + value
        self._cashInventory.add(coinName)

    def getTotalSales(self):
        """return total sales amount"""
        return self._totalSales

    def collectItemAndChange(self):
        """collect item and change after buy in bucket"""
        bucket = Bucket()
        if self._collectItem():
            self._totalSales = self._totalSales + self._currentItem.getPrice()
            bucket.setItem(self._currentItem)
            returnedChanges = self._collectChange()
            bucket.setChanges(returnedChanges)
        else:
            bucket.setItem(None)
            refund_changes = self._refund()
            bucket.setChanges(refund_changes)
        self._currentBalance = 0
        self._currentItem = None
        self._currentlyInsertedCoins = []
        return bucket

    def displayBucket(self, bucket):
        """print bucket value"""
        if bucket.getItem() == None:
            print("item: "+str(None))
        else:
            print("Item: "+str(bucket.getItem().getName()))
        print("Change: ", end='')
        for change in bucket.getChanges():
            if(change != None):
                print(str(change.getName()) +
                      "(value = "+str(change.getValue())+"), ", end='')
        print("", flush=True)


if __name__ == "__main__":
    vendingMachine = VendingMachine()

    print("\n********** Menu *****************")
    print("Item and their price: ")
    print(itemPrice)
    print("Coins and their value")
    print(coinValue)
    print("**********************************\n")
    while True:
        print("\n1. Display Vending Machine stat.")
        print("2. Select item and buy.")
        print("3. Total sales amount.")
        print("4. Reset Machine.")
        print("5. Put item into machine.")
        print("6. Put coin into machine.")

        print("0. Exit", flush=True)
        choice = input("Enter choice: ")
        if choice == '1':
            vendingMachine.displayStats()
        elif choice == '2':
            itemName = input("Enter item name: ")
            price = vendingMachine.selectItemAndGetPrice(
                itemName.lower())
            if(price == -1):
                continue

            print("Item: "+itemName.lower() +
                  " | Price: "+str(price), flush=True)
            buy = input("Want to buy (y/n): ")
            if buy == 'y' or buy == 'Y':
                while price > vendingMachine.getCurrentBalance():
                    insertedCoin = input(
                        "Please insert coin-name (one at a time) || (n) to terminate: ")
                    if(insertedCoin == 'n' or insertedCoin == 'N'):
                        break

                    if insertedCoin.lower() not in coinValue.keys():
                        print("invalid input!", flush=True)
                        continue

                    vendingMachine.insertCoin(insertedCoin.lower())

                bucket = vendingMachine.collectItemAndChange()
                print("\nPlease collect your item and change: ")
                vendingMachine.displayBucket(bucket)
        elif choice == '3':
            print(vendingMachine.getTotalSales(), flush=True)
        elif choice == '4':
            vendingMachine.reset()
        elif choice == '5':
            inputItem = input("Enter item name: ")
            if inputItem.lower() not in itemPrice.keys():
                print("Invalid input! Please insert item only from menu")
                continue
            quantity = input("Enter quantity: ")
            vendingMachine.putItem(inputItem, quantity)
        elif choice == '6':
            inputCoin = input('Enter coin name: ')
            if inputCoin.lower() not in coinValue.keys():
                print("Invalid input! Please insert coin only from menu")
                continue
            quantity = input('Enter quantity: ')
            vendingMachine.putCoin(inputCoin, quantity)
        else:
            exit()
