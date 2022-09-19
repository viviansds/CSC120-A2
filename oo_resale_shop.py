# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
# from computer import Computer
""" This class file takes in an empty nested dictionary named inventory that 
    store information about the computer and its corresponding itemID.

    ResaleShop have four functions: buy(), print_inventory(),refurbish(), 
    and sell() that modifies the nested dictionary.
"""
class ResaleShop:
    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        """initialize ResaleShop class with empty inventory and itemID that begins at 0"""
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID:int = 0
    # What methods will you need?
    def buy(self,computer:dict):
        """Takes in a instance of the class, a dictionary of computer infos and pair with incremented itemID and 
        returns the current itemID as a integer"""
        self.itemID += 1 # increment itemID
        # assign computer information as values associated with the key 'itemID'.
        self.inventory[self.itemID] = computer 
        return self.itemID

    def print_inventory(self):
        """Takes in a instance of the class, print itemID and its corresponding value(computer infos)"""
        # If the inventory is not empty
        if self.inventory:
        # For each item
            for self.item_id in self.inventory:
                # Print its details
                print(f'Item ID: {self.itemID} : {self.inventory[self.itemID]}')
        else:
            print("No inventory to display.")


    def refurbish(self,item_id: int, new_os: Optional[str]=None): 
        """ Takes in a instance of the class, a integer indicating the specific item_id and an optional 
        string for the new_os.Update a computer's price base on its year made and its operating system if 
        given. 'item_id' is different from 'itemID' because item itemID are incremented and only reflect 
        the last item added to the inventory.
        """
        if item_id in self.inventory:
            #access and modify a value in a nested dictionary form
            if self.inventory[item_id]['year_made'] < 2000:
                self.inventory[item_id]['price'] = 0 # too old to sell, donation only
            elif self.inventory[item_id]['year_made'] < 2012:
                self.inventory[item_id]['price'] = 250 # heavily-discounted price on machines 10+ years old
            elif self.inventory[item_id]['year_made'] < 2018:
                self.inventory[item_id]['price'] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.inventory[item_id]['price'] = 1000 # recent stuff
        #If a new_os is given in main.py, update the value associated with the key 'operating_system'
        if new_os is not None:
            self.inventory[item_id]['operating_system'] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def sell(self,item_id: int):
        """ Delete item in the dictionary by removing the key 'itemID'"""
        if item_id in self.inventory:
            del self.inventory[self.itemID]
            print("Item", item_id, "sold!")
        else: 
            print("Item",item_id, "not found. Please select another item to sell.")
