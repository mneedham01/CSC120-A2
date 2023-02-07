from computer import * 

#This establishes the class "ResaleShop" which sets up an inventory (starting with an empty list)
#It can buy new computers and add them to its inventory, sell computers, print its inventory,
#And refurbish the computers by updating its OS and price. 
class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory=[]

    # What methods will you need?
    #The buy method takes in all the necessary information on the computer, creates a computer using the Computer class, 
    #and adds it to the inventory. 
    def buy(self,description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)-> None:
        new_computer=Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.append(new_computer)
    
    #The sell method checks whether a computer is in its inventory, and if it is, removes it. 
    def sell(self, c:Computer) -> None:
        if c in self.inventory:
            self.inventory.remove(c)
        else:
            print("Computer not found.")
    
    #The print inventory method first checks to see if the inventory contains anything, and then loops through it 
    #and asks each computer to print its details. 
    def print_inventory(self)-> None:
        if self.inventory:
            print("Inventory: \n")
            for c in self.inventory:
                c.print_details()
                print()
        else:
            print("Empty inventory.")

    #The refurbish method first checks if the computer is in the inventory, then updates the price based on the year 
    #it was made, and then if it doesn't have the latest operating system, updates it. 
    def refurbish(self,c:Computer) -> None:
        
        if c in self.inventory:
            
            if int(c["year_made"]) < 2000:
                c.update_price(0) # too old to sell, donation only
            elif int(c["year_made"]) < 2012:
                c.update_price(250)  # heavily-discounted price on machines 10+ years old
            elif int(c["year_made"]) < 2018:
                c.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                c.update_price(1000)# recent stuff
            
            new_OS = "MacOS Monterey"

            if c['operating_system'] is not new_OS:
                print("Refurbishing Computer:", c, ", updating OS to", new_OS)
                print("Updating inventory...")
                c.update_OS(new_OS) # update details after installing new OS
                print("Done.\n") 
        else:
            print("Item", c, "not found. Please select another item to refurbish.")



def main():
    myStore= ResaleShop()
    myStore.buy("Computer 1","xxx",1,2, "xxxx",3,5)
    myStore.buy("Computer 2","xxx",1,2, "xxxx",3,5)
    myStore.buy("Computer 3","xxx",1,2, "xxxx",2020,5)
    myStore.print_inventory()
    print()
    myStore.sell(myStore.inventory[0])
    myStore.print_inventory()
    print()
    myStore.sell(myStore.inventory[0])
    myStore.print_inventory()
    print()
    myStore.refurbish(myStore.inventory[0])
    myStore.print_inventory()

if __name__ == "__main__": main()