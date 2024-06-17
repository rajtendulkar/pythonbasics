set1 = {1, 2, 3, 4}
# Another way of declaring set
set2 = set([3, 4, 5, 6])

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
union = set1 | set2
print(f"Union: {union}")

# Intersection
intersection = set1 & set2
print(f"Union: {intersection}")

# Difference
difference = set1 - set2
print(f"Union: {difference}")

# Symmetric Difference
symmetric_difference = set1 ^ set2
print(f"Union: {symmetric_difference}")

# Adding an element to a set
set1.add(5)

# Removing an element from a set
set2.remove(6)  # {3, 4, 5}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")