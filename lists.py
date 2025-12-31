# Python Lists Practice

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
#Output:
Original list: ['apple', 'banana', 'cherry']

# 2. Accessing items
print("First item:", fruits[0])
print("Last item:", fruits[-1])
#Output:
First item: apple
Last item: cherry

# 3. Adding items
fruits.append("orange")   # add at end
fruits.insert(1, "mango") # add at index 1
print("After adding items:", fruits)
#Output:
After adding items: ['apple', 'mango', 'banana', 'cherry', 'orange']

# 4. Removing items
fruits.remove("banana")
popped_item = fruits.pop()
print("After removing items:", fruits)
print("Popped item:", popped_item)
#Output:
After removing items: ['apple', 'mango', 'cherry']

# 5. Loop through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)
#    

# 6. Other operations
print("Number of items:", len(fruits))
fruits.sort()
print("Sorted list:", fruits)
fruits.reverse()
print("Reversed list:", fruits)

