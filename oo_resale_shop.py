from typing import Dict, Union, Optional
from computer import Computer

# itemID = 0
# inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
# Import a few useful containers from the typing module


class ResaleShop:
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID:int = 0
    # What methods will you need?
    def buy(self,computer):
        global itemID
        self.itemID += 1 # increment itemID
        # inventory[itemID].append(computer)
        print(self.itemID)
        self.inventory[self.itemID] = computer
        return self.itemID

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for self.item_id in self.inventory:
            # Print its details
                print(f'Item ID: {self.itemID} : {self.inventory[self.itemID]}')
        else:
            print("No inventory to display.")

    # def update_price(item_id: int, new_price: int):
    # if item_id in inventory:
    #     inventory[item_id]["price"] = new_price
    # else:
    #     print("Item", item_id, "not found. Cannot update price.")
    
    def refurbish_os(self,item_id: int, new_os: Optional[str]):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if self.inventory[item_id]['year_made'] < 2000:
                self.inventory[item_id]['price'] = 0 # too old to sell, donation only
            elif self.inventory[self.item_id]['year_made'] < 2012:
                self.inventory[item_id]['price'] = 250 # heavily-discounted price on machines 10+ years old
            elif self.inventory[self.item_id]['year_made'] < 2018:
                self.inventory[item_id]['price'] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer[item_id]['price'] = 1000 # recent stuff

        if new_os is not None:
            self.inventory[item_id]['operating_system'] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def sell(self,item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
