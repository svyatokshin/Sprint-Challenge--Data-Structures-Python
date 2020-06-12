import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# O(n^2) for a loop within a for loop - original runtime: 4.343478441238403 seconds

# to make it faster we will do O(n log n)

# BST

# new runtime using BST: 0.06677579879760742 seconds
binary = BSTNode(names_1[0])

for name in names_1:  # checks if name is in list
    binary.insert(name)

for name2 in names_2:  # checks if name is in list
    if binary.contains(name2):
        duplicates.append(name2)  # appends duplicates

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
