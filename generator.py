import sys


# List of squares
squares_list = [x * x for x in range(100)]

print(f"Size of list : {sys.getsizeof(squares_list)}")

# Generator for squares
squares_gen = (x * x for x in range(100))

print(f"Size of generator : {sys.getsizeof(squares_gen)}")

# Iterating over the generator
for square in squares_gen:
    print(square)
    if square == 25:
        break
