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
    
    def sell(self, c:Computer) -> None:
        if c in self.inventory:
            self.inventory.remove(c)
        else:
            print("Computer not found.")
    
    def print_inventory(self)-> None:
        if self.inventory:
            print("Inventory: \n")
            for c in self.inventory:
                c.print_details()
                print()
        else:
            print("Empty inventory.")

    def refurbish(self,c:Computer) -> None:
        if c in self.inventory:
            if c.


    def refurbish(item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer =  self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")



def main():
    myStore= ResaleShop()
    myStore.buy("Computer 1","xxx",1,2, "xxxx",3,5)
    myStore.buy("Computer 2","xxx",1,2, "xxxx",3,5)
    myStore.buy("Computer 3","xxx",1,2, "xxxx",3,5)
    myStore.print_inventory()
    print()
    myStore.sell(myStore.inventory[0])
    myStore.print_inventory()
    print()
    myStore.sell(myStore.inventory[0])
    myStore.print_inventory()
    print()
    myStore.sell(myStore.inventory[0])
    myStore.print_inventory()

if __name__ == "__main__": main()