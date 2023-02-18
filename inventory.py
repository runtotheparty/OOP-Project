
from operator import attrgetter

#Define shoe list as global variable
shoe_list = []

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost


    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"""This the {self.product}, it costs £{self.cost}, it is from {self.country}. 
There are {self.quantity} of this product remaining. The product code is {self.code}\n""")


#==========Functions outside the class==============
def read_shoes_data():
    empty_shoe_list()
    inv = open("inventory.txt", "r")
    rl = inv.readlines()
    for line in rl:
        if "Country,Code,Product,Cost,Quantity" in line:
            continue
        else:
            contents = line.strip().split(",")
            temp_country = contents[0]
            temp_code = contents[1]
            temp_product = contents[2]
            temp_cost = int(contents[3])
            temp_quantity = int(contents[4])
            contents[2] = Shoe(temp_country, temp_code, temp_product, temp_cost, temp_quantity)
            shoe_list.append(contents[2])
    inv.close()

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# overwrite the text file - to be used if shoe_list is amended
def over_write():
    overwrite_list = []
    amended_data = open("inventory.txt", "w")
    for i in shoe_list:
        temp_country = i.country
        temp_code = i.code
        temp_product = i.product
        temp_cost = str(i.cost)
        temp_quantity = str(i.quantity)
        temp = [temp_country, temp_code, temp_product, temp_cost, temp_quantity]
        overwrite_list.append(temp)

    # joining nested loops here to avoid  type error as more than one list in read_tasks https://bit.ly/3PvRAPg
    overwrite = "\n".join(','.join(l) for l in overwrite_list)
    amended_data.write(overwrite)
    amended_data.close()


def empty_shoe_list():
    shoe_list.clear()

def capture_shoes():
    country_from = input("What country: ")
    SKU_code = input("Please enter SKU code: ")
    product_name = input("Please enter product name: ")

    try:
        shoe_cost = int(input("How much does this shoe cost: "))
        quantity = int(input("What is the quantity of this product: "))
        product_name = Shoe(country_from, SKU_code, product_name, shoe_cost, quantity)
        shoe_list.append(product_name)

    except ValueError:
        print("\nInvalid input. Please enter a valid number. Returning to menu. \n")

    return shoe_list


def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
    for i in shoe_list:
        print(i)


def re_stock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


    # attrgetter from https://stackoverflow.com/questions/6085467/python-min-function-with-a-list-of-objects

    min_num = min(shoe_list, key=attrgetter('quantity'))
    print (min_num)

    while True:
        try:
            add_stock = int(input("Please enter the amount of stock you would like to add for this shoe: "))
            break
        except:
            print("That was not a number, try again.")
    revised_quantity = min_num.quantity + add_stock
    # replace object in the list with updated details.
    for i in range(len(shoe_list)):
        if shoe_list[i] == min_num:
            shoe_list[i].quantity = revised_quantity

    #write the list back to the txt file
    over_write()



def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        what_shoe = input("Please enter the code of the item or the product name: ")
        for i in shoe_list:
            if what_shoe == i.code or what_shoe == i.product:
                return i

        print("That is not a recognised product or code, try again.")
        

def value_per_item():
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    for i in shoe_list:
        value = i.cost * i.quantity
        print(f"\nThe total value of {i.product} is £{value}\n")



def highest_qty():
    # attrgetter from https://stackoverflow.com/questions/6085467/python-min-function-with-a-list-of-objects

    max_num = max(shoe_list, key=attrgetter('quantity'))
    print (f"\nThe {max_num.product} has the highest quantity at {max_num.quantity}. It is for sale. \n")
    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# START
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''


read_shoes_data()



while True:
    #presenting the menu to the user and making sure that the user input is coneverted to lower case. Start with admin only menu

    menu = input('''Select one of the following Options below:
get data - Get any updated data from the database
new shoes - Add shoes
view all - View all products
restock - view shoes with lowest quantity and request re-stock
search shoe - Seach for a shoe
highest quantity - Find the product with the highest quantity
vpa - Show the total value of all the products
: ''').lower()
    
    if menu == "get data":
        read_shoes_data()

    elif menu == "new shoes":
        capture_shoes()
        over_write()

    elif menu == "view all":
        view_all()

    elif menu == "restock":
        re_stock()

    elif menu == "search shoe":
        search_result = seach_shoe()
        print(search_result)

    elif menu == "highest quantity":
        highest_qty()

    elif menu == "vpa":
        value_per_item()

    else: 
        print("Oops, wrong input, try again.")

#END