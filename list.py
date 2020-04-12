#This program makes a simple list

list_items = []
add_item = 'y'
name = input("What is your name? ")
item_number = 1 

while(add_item == 'y'):    
    list_items.append(input('Item to add: '))
    add_item = input("Would you like to add another item? ")
    
if(add_item != 'y'): #Show the list
    print('------------------------')
    print(name + "'s List")
    
    for i in list_items: 
        print(str(item_number) + ". " + i)
        item_number += 1