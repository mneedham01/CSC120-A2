from computer import * 

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory=[]

    # What methods will you need?
    def buy(self,description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)-> None:
        new_computer=Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.append(new_computer)
    
    def sell(self, c:Computer)- >None:
        if c in self.inventory:
            inventory.remove(c)
        else:
            print("Computer not found.")

def main():
    myStore= ResaleShop()
    myStore.buy("a","a",1,2, "a",3,5)
    print(myStore.inventory)
    myStore.sell(myStore.inventory[0])