# Creating a dictionary
my_dict = {
    "name": "Smith",
    "age": 42,
    "nationality": "French",
    "status": "Married",
    "city": "Munich"
}

# Accessing elements
print(my_dict["name"])

# Adding a new key-value pair
my_dict["email"] = "sm@gmail.com"

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, ":", value)
