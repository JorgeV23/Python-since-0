a = " Hello World"
print(len(a))# longitud

b=a[0]#First character

c=a.strip()#The strip() method removes any leading, and trailing whitespaces.You can specify which character(s) to remove, if not, any whitespaces will be removed.
print (c)
print(len(c))

d=c.upper()
print(d)

d=c.lower()
print(d)

e=c.replace("Hello","jelou")
print(e)


#-------FORMAT STRINGS
#"F-STRINGS"
myname="Jorge"
age=18
txt="Hello my name is {} and my age is {}"
print (txt.format(myname,age))
#PLACEHOLDERS AND MODIFIERS
myname="Jorge"
age=18
txt=f"Hello my name is {myname} and my age is {age+18}"
print (txt)

##String methods:https://www.w3schools.com/python/python_strings_methods.asp