#int1 = 2+1
#int2 = 2+1
#int3 = int1 + int2
#print(int3)

#n = 1
#while n <= 3:
#    answer = input()
#    print(str(n) + ". " + answer)
#    n += 1

#item1 = input("Add an item: ")
#item2 = input("Add an item: ")
#item3 = input("Add an item: ")
#print(" ")
#print("HERE IS YOUR LIST")
#print("1. " + item1)
#print("2. " + item2)
#print("3. " + item3)

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



