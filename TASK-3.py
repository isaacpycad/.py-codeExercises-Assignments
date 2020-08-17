#1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
b=[]
b.append(-1)
b.append(10.5)
b.append("string")
b.append(10+10j)
print(b)
for i in b:
    print(type(i))
print(type(b))
print(type(tuple(b)))
print(type(set(b)))
print(type((b)))

#2. Create a list of size 5 and execute the slicing structure.
b=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17]
c=b[0:2]
print(c)
c=b[1:3]
print(c)
c=b[1:16:3]
print(c)
c=b[::-1]
print(c)
c=b[::-2]
print(c)

#3. Write a program to get the sum and multiply of all the items in a given list.
b=[1,2,3,5,6]
c=1
for i in b:
    c=c*i
    print(c)


#4. Find the largest and smallest number from a given list.


b=[1,2,3,4,5,6,7,8,9,2,7,45]
print(max(b))
print(min(b)
#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

b=[1,2,3,4,5,6,7,8,9,34,56,55,43,44,66,65,54,43,45,65,77,66,54,325,26,56,245,62,45,62,57,547,2,7,45]
c=[]
for i in b:
    if i%2==0:
        c.append(i)
    else:
        continue
print(c)

#6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

b=[]
for i in range(1,31):
    if i<6 or i >25:
        b.append(i**2)
    else:
        b.append(i)
print(b)
#7. Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]
array = [[1,3,5,7,9,10],[2,4,6,8]]
new=array[0]
neww=array[1]
new.pop()
for i in neww: new.append(i)
print(new)



#8. Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
c={}
c.update(a)
c.update(b)
print(c)

#9 Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

nn=dict()
for x in range(1,10):
    nn[x]=x*x
print(nn)

#10. Write a program which accepts a sequence of comma-separated numbers from console and generate a
# list and a tuple which contains every number. Suppose the following input is supplied to the program:
a=input("Enter: ")
print(a.split(',')," - ",tuple(a.split(","))
