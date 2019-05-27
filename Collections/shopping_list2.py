# Imports
import os

# Variables
shopping_list = []

# Clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Show the help screen
def show_help():
    clear_screen()
    print()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see the list of items.
Enter 'HELP' for this help.
Enter 'REMOVE' to remove an item from the list.
""")

# Show the shopping list
# REWRITTEN WITH ENUM
def show_list():
    clear_screen()
    print("Shopping list:")
    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
    print("-"*10)

# Remove an item from the list
def remove_item():
    show_list()
    item_to_remove = input("What would you like to remove?  ")

    try:
        shopping_list.remove(item_to_remove)
    except ValueError:
        pass
    
    show_list()

# Add an item to the list
def add_to_list(item):
    show_list()
    
    if shopping_list:
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list.\n"
                         "> ".format(item))
    else:
        position = 0
        
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
            
    show_list()

# ##### PROGRAM START   #####
# Show help
show_help()

while True:
    new_item = input("> ")
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_item()
        continue
    else:
        add_to_list(new_item)

# ##### PROGRAM END   #####
show_list()
