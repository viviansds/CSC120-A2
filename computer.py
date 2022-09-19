class Computer:

    # What attributes will it need?
    """ This class file takes in various information about the computer. 
    Computer only have one functions create_computer() that takes in the 
    information and return a dictionary that can be added to the inventory 
    in oo_resale_shop.py.
    """
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made =  year_made
        self.price = price
    # What methods will you need?
    """Create the computer into a dictionary with the given arguments"""
    def create_computer(description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):

        return {'description': description,
                'processor_type': processor_type,
                'hard_drive_capacity': hard_drive_capacity,
                'memory': memory,
                'operating_system': operating_system,
                'year_made': year_made,
             'price': price
      }

