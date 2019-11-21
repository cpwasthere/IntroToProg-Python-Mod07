# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ChrisPerry,11/4/19,Added code to complete assignment 5
# ChrisPerry,11/5/19,Added append functionality
# ChrisPerry,11/5/19,Added custom dictionary and dictionary.keys logic to verify
# input keys are listed before we attempt to remove them.
# ChrisPerry,11/6/19,Final code clean up and commenting.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# We're checking for the existence of out file in memory.
# If the file isn't there, using 'w+' creates it and also writes 
# to the file in memory
if not objFile:
    open(objFile, 'w+').close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
            print(objRow)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Collecting input for our user's tasks and priorities, and
        # and ensuring the values are strings, making them a dictionary row and
        # then using that to append to our file in memory.
        strData = open(objFile, "a")
        task = input("What task would you like to add? ")
        prior = int(input("What priority should this task have? "))
        lstRow = [task, str(prior)]
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
        # strData.write(lstRow[0] + ',' + lstRow[1] + '\n')
        strData.close()
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        strData = open(objFile, "a")
        taskd = input("What is the name of the task? ")
        
        # creating a searchable dictionary from our list table.
        # using the keys function for dictionaries so we can
        # just ask the user for the task name (key) and auto pull 
        # the priority (value)
        d = dict((i['Task'], i['Priority']) for i in lstTable)
        if taskd in d.keys():
            print("Task found! Removing.. ")
            priord = d[taskd]
        else:
            print("Task not found. Try again. ")
            continue
        # Taking our input after verifying it's in the dictionary
        # and removing the selected task out of our list table in memory
        lstRow = [taskd, str(priord)]
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.remove(dicRow)
        strData.close()
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would you like to save your data?: ")
        # while loop to present a yes or no prompt to the user for saving.
        while True:
            try:
                saveExit=input("Enter 'y' or 'n': ")
                if saveExit == 'y':
                    with open("ToDoList.txt", "w") as output:
                        output.write(str(lstTable) + "\n")
                    break
                elif saveExit == 'n':
                    break
                else:
                    print("Please enter 'y' or 'n'")
                    continue
            except ValueError:
                print("Invalid choice. Please Try Again")
        exit    
        
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
