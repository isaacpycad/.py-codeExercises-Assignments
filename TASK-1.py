
# TASK ONE: NUMBERS AND VARIABLES
# 1.	Create three variables in a single a line and assign different values to them and make sure their data types are different.
# Like one is int, another one is float and the last one is a string.
x=9.9878
y=3+5j
z=True

#2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
x=5+6j
y=7
x,y=y,x
print(y)

#3.Swap two numbers using the third variable as the result name and do the same task without using any third variable.
x = 77
y = 999
x = x + y

y = x - y
x = x - y
print("new x=", x, "new y =", y)

#4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
#python 2.x
x = raw_input('enter')
print 'x'

#python 3.x
x = input('enter')
print(x)

##5. 	Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.

x,y=[int(a) in a input('enter two nums').split(' ')]
z=x+y
print(z)

# 6. 	Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
x=eval(input('enter value to check data type'))
print('data type of entered value is =',type(x))


# 7. 	Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/) - Variable Conventions to write
Variable = 10
variable = 12
VARIABLES = 14

# 8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again.
# Will it change the value. If Yes then Why?
#answer-yes because here we are talking about to change the data type of the value a new data type will be a different object type.