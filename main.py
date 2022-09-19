#Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union
# Import class ResaleShop and Computer 
from oo_resale_shop import ResaleShop
from computer import Computer
""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
    
def main():
    
    # First, let's make a computer

    new_computer= Computer.create_computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
    #Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    shop = ResaleShop()

    # Add it to the resale store's inventory
    print("Buying", new_computer["description"])
    print("Adding to inventory...")
    computer_id = ResaleShop.buy(shop,new_computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(shop)
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    ResaleShop.refurbish(shop,computer_id,new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(shop)
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    ResaleShop.sell(shop,computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(shop)
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
