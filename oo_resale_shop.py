from typing import Dict, Union, Optional
from computer import Computer

itemID = 0
inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
# Import a few useful containers from the typing module


class ResaleShop:
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID:int = 0
    # What methods will you need?
    def buy(computer):
        global itemID
        itemID += 1 # increment itemID
        # inventory[itemID].append(computer)
        inventory[itemID] = computer
        return itemID

    def print_inventory():
    # If the inventory is not empty
        if inventory:
        # For each item
            for item_id in inventory:
            # Print its details
                print(f'Item ID: {itemID} : {inventory[itemID]}')
        else:
            print("No inventory to display.")

    def refurbish(item_id: int, new_os: Optional[str]):
        print(inventory)
        if item_id in inventory:
            computer = inventory[item_id] # locate the computer
            if inventory[item_id]['year_made'] < 2000:
                computer[item_id]['price'] = 0 # too old to sell, donation only
            elif inventory[item_id]['year_made'] < 2012:
                computer[item_id]['price'] = 250 # heavily-discounted price on machines 10+ years old
            elif inventory[item_id]['year_made'] < 2018:
                computer[item_id]['price'] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer[item_id]['price'] = 1000 # recent stuff

        if new_os is not None:
            inventory['operating_system'] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def sell(item_id: int):
        if item_id in inventory:
            del inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
