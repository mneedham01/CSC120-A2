#Establishes the class "Computer" which holds all the necessary information about the computer, 
#can update the price and operating system, and can print out the details about the computer. 
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
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory:int, operating_system:str, year_made:int, price:int)-> None:
        self.description= description
        self.processor_type= processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system=operating_system
        self.year_made= year_made
        self.price= price 

    # What methods will you need?
    #This method updates the operating system-- it requires input for what the new operating system will be
    def update_OS(self, new_operating_system) -> None:
        self.operating_system= new_operating_system

    #This method updates the price and also requires input for what the new price will be 
    def update_price(self, new_price) -> None:
        self.price=new_price
    
    #This method prints out all the information about the computer 
    def print_details(self)-> None:
        print(self.description)
        print("Processor Type:",self.processor_type)
        print("Hard Drive Capacity:",self.hard_drive_capacity)
        print("Memory:",self.memory,"GB")
        print("Operating System:",self.operating_system)
        print("Year Made",self.year_made)
        print("Price:", self.price)