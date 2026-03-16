#declare a variable global
x =  "awesome"
def myfunc():
    global x  # variable x declared as global
    x = "fantastic" # x varible in function can be used outside function
    print("python is " + x)
myfunc()
print("python is "+ x)
