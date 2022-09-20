# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
""" This class file takes in an empty nested dictionary named inventory that 
    store information about the computer and its corresponding itemID.

    ResaleShop have five functions: buy(), print_inventory(),refurbish(), 
    update_price(), and sell() that modifies the inventory.
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
        #assign computer information as values associated with the key 'itemID'.
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
            #check to see if the computer is in the inventory dictionary
            if item_id in self.inventory:
                #assign "computer" as the name for the values associated with the key "itemID" in the nested dictionary called ""inventory
                computer = self.inventory[item_id]
                #access and modify the computer dictionary that is created in computer.py 
                if int(computer["year_made"]) < 2000:
                    computer["price"] = 0 # too old to sell, donation only
                elif int(computer["year_made"]) < 2012:
                    computer["price"] = 250 # heavily-discounted price on machines 10+ years old
                elif int(computer["year_made"]) < 2018:
                    computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    computer["price"] = 1000 # recent stuff
                #If a new_os is assigned in main.py and is placed as the arguments of the refurbish() function, update the value associated with the key 'operating_system'
                if new_os is not None:
                    computer['operating_system'] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


    def update_price(self,item_id: int, new_price: int):
        """This is a function that takes in an item_id and a new price, updates any arbitrary 
        assigned price to a computer in the inventory, regardless of the year made. If it is not in the inventory, 
        prints error message.
        """
         #check to see if the computer is in the inventory dictionary
        if item_id in self.inventory:
            #access and modifies a nested dictionary by assigning a new value for the key "price"
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self,item_id: int):
        """ Delete item in the dictionary by removing the key 'itemID'"""
        #check to see if the computer is in the inventory dictionary
        if item_id in self.inventory:
            #delete the specific itemID key and its associated value
            del self.inventory[self.itemID]
            print("Item", item_id, "sold!")
        else: 
            print("Item",item_id, "not found. Please select another item to sell.")
