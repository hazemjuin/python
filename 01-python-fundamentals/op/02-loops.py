
# In JavaScript
# for (var i=0; i<1; i++) {
# console.log
# }



# IN PYTHON
# range = function that returns a sequence of numbers
#     start : inclusive has a default value fo 0
#     stop : exclusive and required
#     step : not required and default l can be + or -
#     example :
#         range(0,10) => (0,1,2,3,4,5,6,7,8,9)


# for i in range(0,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)    
    # for j in range(0,i):
    #      print(j)
    
# for i in range(0,10,-2):
#     print(i)    
    # for j in range(0,i):
    #      print(j)
# for i in range(10):
#     print(i)



superheros = ["superman" , "batman" , "spiderman" , "antman" , "jedi"]
for i in range (0, len(superheros)):
        print(superheros[i])

    # for hero in superheros :
    # print(hero)

user = {
        'first_name' : "John",
        'last_name' : "Smith",
        'age' : 41,
        'is_admin' : False,
        'marks' : [10,9,8,10],
        'friends' : ['one', 'alex', 'tow', 'Max']

}

# for key in user.keys():
        # print(f"KEY {key} *** {user[key]}")
# print(user.items())
for value in user.values():
        print(value)