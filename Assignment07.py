# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Using Pickling and Error Handling in Python
# ChangeLog (Who,When,What):
# ChrisPerry,11/19/19, Added additional functions to code
# ChrisPerry,11/20/19, Added additional final edits
# ------------------------------------------------------------------------ #




import pickle

task = str(input("Enter a Task: "))
priority = int(input("Enter a Priority: "))
tasklist = [task, priority]
print(tasklist)


# Let's pickle some data

picklefile = open("AppData.dat", "ab")
pickle.dump(tasklist, picklefile)
picklefile.close()

# Now let's read back our pickled data

picklefile = open("AppData.dat", "rb")
pickledata = pickle.load(picklefile)
picklefile.close()
print(pickledata)