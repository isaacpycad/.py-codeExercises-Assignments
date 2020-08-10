#TASK-1 1. Write a program using function USINto reverse a string.

#Sample data: “1234abcd”

#Expected Output: “dcba4321”


def f1(str):
    z=len(str)
    q=1
    for x in range(z):
        print(str[z-q],end='')
        q+=1
f1('1234abcd')

#TASK-2 Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.

def ul(s):
    up = sum(1 for i in s if i.isupper())
    low = sum(1 for i in s if i.islower())
    print('up-',up,'low-',low)

ul('IsAAcChriSti')

#TASK-3
#Create a functioN that takes a list and returns a new list with unique elements of the first list.

def unique(l):
    set_lst=set(l)
    unq_lst=list(set_lst)
    for x in unq_lst:
        print(x,end="")

unique([1,1,2,2,2,2,4,4,4,8,9,3,4,5,3,3])

#TASK-4  Write a program that accepts a hyphen-separated sequence of words as input and prints




hvalues=[n for n in input('insert hyphen seperated values').split('-')]
hvalues.sort()
print('-'.join(hvalues))






#TASK-5
# the words in a hyphen-separated sequence after sorting them alphabetically.
def f1():
    txt = [x for x in input('Enter Hyphen-seperated text').split('-')]
    txt.sort()
    print('-'.join(txt))

f1()

#Task-6 Define a function that can receive two integral numbers in string form and compute their sum and print it in console.



def intregal(a,b):
    x=int(a)
    y=int(b)
    z=x+y
    print(z,type(z))

intregal('10','11')

#TASK-7  Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.


def strln(s1, s2):
    if len(s1) > len(s2):
        print('S1 LONGER ', s1)
    elif len(s1) < len(s2):
        print('S2 LONGER: ', s2)
    else:
        print('BOTH ARE EQUAL')

strln('hello','hello')

#TASK-8   Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)

#TASK-9 Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between
# 0 and limit with a label to identify the even and odd numbers.


def showNumbers(limit):
for i in range(0,limit+1):
if i%2==0:
print(“EVEN ”)
else:
print(“ODD”)

showNumbers(5)

#TASK-10 Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
l1 = range(1,21)

l2 = [i for i in l1 if i % 2 == 0]
print(l2)

#TASK-11 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, l))

print(even)

#TASK-12  Write a function to compute 5/0 and use try/except to catch the exceptions


def excptn(x,y):
    try:
        print(x/y)
    except ArithmeticError:
        print('Cant divide by Zero y must be >0')

excptn(4,0)
#TASK-13 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567
lst = [[1, 2, 3], [4, 5], [6,7, 8, ]]  # List to be flattened
flat = []

for i in range(len(lst)):  # Traversing through the main list
    for j in range(len(lst[i])):  # Traversing through each sublist
        flat.append(lst[i][j])  # Appending elements into our flat_list

print("Flattened List:", flat)
#TASK-14
def foo():

    try:

        return 1

    finally:

        return 2

k = foo()

print(k)
#O/P-IT WILL PRINT 2


(ii)


def a():
    try:

        f(x, 4)

    finally:

        print('after f')

    print('after f?')


a()
#O/P- ERROR "F" NOT DEFINED
