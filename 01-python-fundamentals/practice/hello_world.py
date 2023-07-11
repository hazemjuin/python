# #1
print("Hello World")

# #2a
name = "John Doe"
print("Hello", name, "!")

# #2b
name = "John Doe"
print("Hello " + name + "!")

# #3a
num = 42
print("Hello", num, "!")

# #3b
num = 42
print("Hello " + str(num) + "!")

# NINJA BONUS
num = 42
print("Hello", str(num) + "!")  # Resolving the error without changing the + sign

# #4a
food_one = "pizza"
food_two = "sushi"
print("I love to eat {} and {}.".format(food_one, food_two))

# #4b
food_one = "pizza"
food_two = "sushi"
print(f"I love to eat {food_one} and {food_two}.")

# NINJA BONUS
string_example = "  hello  "
print(string_example.strip())  # Removes leading and trailing whitespace
print(string_example.upper())  # Converts the string to uppercase
print(string_example.lower())  # Converts the string to lowercase
print(string_example.replace("l", "L"))  # Replaces all occurrences of "l" with "L"
print(string_example.startswith("h"))  # Checks if the string starts with "h"
print(string_example.endswith("o"))  # Checks if the string ends with "o"
