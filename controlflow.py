
# Demo if else statement
def check_value_x(x):
    if x > 110:
        print(f"x is greater than 110: {x}")
    elif x < 110:
        print(f"x is less than 110: {x}")
    else:
        print("x is equal to 110")


# Conditional Statements
check_value_x(20)
check_value_x(200)
check_value_x(110)

# For Loop
print("For loop from 1 to 10:")
for i in range(1, 11):
    print(i, end=' ')
print()

# While Loop
print("While loop from 1 to 10:")
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# Break Statement
print("Break statement example:")
break_at=8
for i in range(1, 10):
    if i == break_at:
        print(f"\nBreaking the loop at i = {break_at}")
        break
    print(i, end=' ')
print()

# Continue Statement
print("Continue statement example for odd numbers:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=' ')
print()

# Pass Statement
print("Pass statement example:")
for i in range(1, 11):
    if i == 9:
        # The pass statement is used as a placeholder for future code.
        # When the pass statement is executed, nothing happens,
        # but you avoid getting an error when empty code is not allowed.
        pass
    print(i, end=' ')
print()
