##You can comment your code using "##"

##----------------------------VARIABLES-------------------------------------
    ##You don't need to declare the data type of each variable
a=1
b=2
c=a+b
name="Carlos"
    ##Many values to multiples variables
A,B,C,D=1,2,3,4
    ##One value to multiple varibles
x=y=z="Hola"

##----------------------------Output variables------------------------------
    ##You can print multiple variables using print() function
print(a,b) ##This will print 1 2
print(c) ##This will print 3
    ##You also can do math operation with the variables
print(a+b) ##This will print 3
##print(a+name) ##This will show an error

##---------------------------Global variables---------------------------------

##Global variables are the one that are declared out of a function
# But if you declare a variable into a function this will be a local variable and only can be used inside the function
# Example
Y="Awesome"
print("The first word is "+ Y)
def printY():
    Y="Incredible"
    print("The last word is " + Y)
printY()

#global keyword: You can use the gloal keyword for changing the variable value or to declare a global variable into a function
def changeY():
    global Y
    Y="New awesome"

changeY()

print("The new is "+ Y)