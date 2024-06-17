# Getting integer input
int_user_input = int(input("Enter an integer: "))
print(f"Integer obtained: {int_user_input}")

# Getting float input
float_user_input = float(input("Enter a float: "))
print(f"Float obtained: {float_user_input}")

# Getting string input
string_input = input("Enter a string: ")
print(f"String obtained: '{string_input}'")

# Getting boolean input
bool_input_str = input("Enter a boolean value (True/False): ")
bool_input = bool_input_str.lower() in 'true'
print(f"Boolean obtained: {bool_input}")
