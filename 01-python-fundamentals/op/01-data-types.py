# this is a comment this line will not be interpreted

# this 


# How to declare variables
# JavaScript var variableName = value

# python is snake we are going to use snake_case_naming_convention


variable_name = "value"

GLOBAL_VARIABLE = "python"
PORT = 5000
APP_NAME = "WEB_APP"

# DATA TYPES
# string
first_str = 'hello world'
name = 'john'
# numbers
    # integers
age = 41
    # floats
bmi = 2.75

# boolean
voted = True
is_admin = False
# nonetype
permit = None
# print(name, age, bmi, is_admin)
# formatted string
# print(f"User name : {name} his age {age} years and his BMI equal to {bmi}")






# print(f"None : {type(permit)}\nName : {type(name)}")

str_age = str(age)
float_age = float(age)
# print(f"AGE : {type(age)}\nSTR_AGE : {type(str_age)}\nFLOAT_AGE{type(float_age)}")
# print(len(name), name.upper(), first_str.split(' '))

# complex

# array in JavaScript == List in Python
# INDEX   0                                        len(list)-1
my_list = [1,2,3,"45",5, name, age, is_admin, bmi, ["yes", "no", None]]

# print(len(my_list))
# print(my_list[-1])
# print(my_list[-2])
# # print(my_list[0:5])
print(my_list)
my_list.append(first_str)
print(my_list)
#   DELETE last item from the list
my_list.pop()
print(my_list)

