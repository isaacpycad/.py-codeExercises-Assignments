#1.	Write a program to Python find the values which is
#not divisible 3 but is should be a multiple of 7.
#Make sure to use only higher order function.

limit=int(input("Enter the limit: "))
print([i for i in range(0,limit) if i%3!=0 and i%7==0])

#2. Write a program in Python to  multiple the element of list by itself using a
# traditional function and pass the function to map to complete the operation.
l=[1,2,3,4]
n=[]
def new():
    for i in l:
        n.append(i*i)

#3. Write a program to Python find out the character in a string which is uppercase using list comprehension

inp=str(input("Enter the String"))
c = [i for i in inp if i.isupper()]
print(c)

#4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should maps the students with their respective subjects. Let’s see how to do this
# using for loops and dictionary comprehension. HINT-Use Zip function also
#Student = ['Smit', 'Jaya', 'Rayyan']
#capital = ['CSE', 'Networking', 'Operating System']

# USING DICTIONARY COMPRE.
st = ['Smit', 'Jaya', 'Rayyan']
ca = ['CSE', 'Networking', 'Operating System']
newd={st[i]:ca[i] for i in range(0, len(st))}
print(newd)
#USING ZIP FUNCTION
st = ['Smit', 'Jaya', 'Rayyan']
ca = ['CSE', 'Networking', 'Operating System']
newdic=zip(st,ca)
print(dict(newdic))

#5.  Learn More about Yield, next and Generators
#yield
'''Yield is used to transform a function to a generator.
with return in method it stops the execution, but generator with yield can resume the execution from where it left.
it works same like return, stops the execution and sends the value back to caller'''
#generator
'''Generators are basically a way to create iterators, its a function which returns the value(Yield)
and iterate it over and over'''
#next()
'''Next is an inbuild method which gets the next item frm iterator by calling method __next__.'''
#6. 	Write a program in Python using  generators to reverse the string. Input String = “Consultadd Training”
def fun(str):
    yield str[::-1]
inp=str(input("Please enter a string: "))
var=fun(inp)
print(var.__next__())

#7
'''decorator adds extra functionality to existing function without affecting it.'''
def division(a,b):
    print(a/b)

def f2(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

division1=f2(division)
division1(2,4)

#8
'''What is front end 
Front end is basically client side, whatever a user interacts with. a
nd back end is server side which can be interact by developers and organization members only.
Front end technology involves building the user interface like websites or web applications. 
which includes design of UI, structure, animation and flow of the website.
Front end Technologies
HTML , CSS, JavaScript, Angular, PHP - Facebook'''

