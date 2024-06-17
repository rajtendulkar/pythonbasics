# List
my_list = [3, 4, 5, 6, 7]
print(f"List value: {my_list}")

print("Iterating over my_list:")
for item in my_list:
    print(item)

# Tuple
my_tuple = (21, 32, 43, 54, 65)
print(f"Tuple value: {my_tuple}")

print("\nIterating over my_tuple:")
for item in my_tuple:
    print(item)

# Creates a range of numbers from 5 to 21
my_range = range(5, 21)
print(f"Range value: {list(my_range)}")

for item in my_range:
    print(item)

# Append to the list
my_list.append(66)
print(f"Now List is : {my_list}")

# Create a sum of all number in the range
range_sum = sum(my_range)
print(f"Sum of all numbers in range : {range_sum}")

# Combining different data types
list_from_tuple = list(my_tuple)
new_list = my_list + list_from_tuple
print(f"Combined list: {new_list}")
