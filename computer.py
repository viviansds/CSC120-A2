class Computer:

    # What attributes will it need?

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
# new_computer=Computer.create_computer("Mac Pro (Late 2013)",
#     "3.5 GHc 6-Core Intel Xeon E5",
#     1024, 64,
#     "macOS Big Sur", 2013, 1500)
# print(new_computer)

    # What methods will you need?