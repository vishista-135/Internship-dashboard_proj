
shopping_list = []

print ("What should we pick up at the store?")
print ("Enter 'DONE' to stop adding the items to list.")


while True:
    New_item = input("Enter the item: ")
    
    if (New_item == 'DONE'):
        break
    shopping_list.append(New_item)
    
print ("Here is your list items:")
for item in shopping_list:
    print (item)


