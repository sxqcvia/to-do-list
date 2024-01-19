#Zhiyin
#1/10
#To-Do List


shoppinglist = [] 
print("""welcome to the shopping list! type in numbers 1-5 for options 
      
1. Add a task to the to-do list 
2. View the current to-do list 
3. Mark a task as completed
4. Remove a task from the to-do list 
5. Sort the list alphabetically
6. Print the # of Items on the To-do List
7. Remove all tasks from the to-do list
8. Exit the program""")

while True: 
    choice = int(input("what do you want to do (1-8)"))
    if 1<= choice <= 8:
        if choice == 1: 
            shoppinglist.append(input("add to list:"))
        if choice == 2:
            print(shoppinglist)
        if choice == 3: 
            completed = int(input("which number on the list have you completed?")) - 1 
            shoppinglist[completed]  = "[X]" + shoppinglist[completed]
        if choice == 4: 
            remove = input("which list item would you like to remove?(name the exact list item!)")
            if remove in shoppinglist: 
                shoppinglist.remove(remove)
            else: 
                print("item not in list")
                remove = input("which list item would you like to remove?(name the exact list item!)")
        if choice == 5:
            shoppinglist.sort()
            print(shoppinglist)
        if choice == 6:
            print(len(shoppinglist))
        if choice == 7:
            shoppinglist.clear()
            print("List cleared")
        if choice == 8: 
            quit()
    else:
        print("pick 1-8")