class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)-> None:
        self.description= description 
        self.processor_type= processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system=operating_system
        self.year_made= year_made
        self.price= price 

    # What methods will you need?
    def update_OS(self, new_operating_system) -> None:
        self.operating_system= new_operating_system

    def update_price(self, new_price) -> None:
        self.price=new_price
        
