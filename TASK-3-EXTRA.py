#1
l=[]
for i in range(0,5):
    c=input("Enter: ")
    l.append(c)
print(l)

#2

l=["4","i","43.10","dsfew"]
print(l[0:3])
print(l[2:3])
print(l[::-1])
print(l[::-2])
print(l[0:5:1])

#3

x=[]
y=[]
z=[]
temp=[]
for i in range(1,9):
    c=i*100
    x.append(c)
for i in range(1,10):
    y.append(i)
for i in range(1,6):
    i*=10
    z.append(i)
y.insert(5,z)
x.insert(5,y)
print("Creation of List: ",x)
for i in range(0,4):
    temp.append(x[5][i])
print("\n1- Access list [1, 2, 3, 4]: ",temp)
temp=[]
temp.append(x[6])
temp.append(x[7])
print("2- Access list [600, 700]: ",temp)
print("3- Access list [100, 300, 500, 600, 800] ")
print("4- Access list reverse: \n",x[::-1])
print("5- Access list [10]: ",x[5][5][0])
c=0
print("5- Access list [10]: ",x[5][5][0])
print("6- Access list [ ]: \n")
for i in x:
    if i==" ":
        c+=1
        print("6- Access list []: ",x[i])
    if c>1:
        print(" got elements: ",c)
if c==0:
    print("there is no such a elemnt has " " in it.")

#4
for i in range(0,100):
    print(i)
for i in xrange(0,100):
    print(i)

#5
#Immutable, so good for important and not changing data Needs less memory,FastervGives more security

#6

for i in range(0,100):

    if i%3==0 and i%2==0:
        print(i)


#7

strr=str(input("Enter the String"))
str=strr[::-1]
print("Reverse string is -- ",str)
olist=""
chkstr="aeiouAEIOU"
c=0
for i in str:
    c+=1
    for j in chkstr:
        if i==j:
            olist+=i
            print(i,"-- Index value is:",c)
#8

str="str(input(""))vishal is here and there as wellhere and there here and therehere and there"
newstr=""
c=0
x=len(str)+1
for i in str:
    if i!=" ":
        newstr+=i
    elif i==" ":
        if len(newstr)%2==0:
            print(newstr)
            newstr=""
            c+=1
        else:
            pass
            newstr=""
if len(newstr)%2==0:
    print(newstr)
    c+=1
print("\n\nTOTAL EVEN WORDS IN THE STRING: ",c)

#9
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
y = []
c = 0
for i in x:
    for j in x:
        if i + j == 8:
            c += 1
            print("Double pair number", c, "is:", i, j)
c = 0
print("\n")
for i in x:
    for j in x:
        for k in x:
            if i + j + k == 8:
                c += 1
                print("Tripple Pair number", c, "is:", i, j, k)

#10

odd = []
even = []
inlist = []
e=o=0
x=y=0
while x<5 and y<5:
    innumber=int(input("enter the number : "))
    if innumber in range(0,50):
        if innumber%2==0:
            even.append(innumber)
            e+=1
            x+=1
        elif innumber%2!=0:
            odd.append(innumber)
            o+=1
            y+=1
        else:
            print("enter the number in given range")
    else:
        if len(odd)==5:
            avg=sum(odd)/len(odd)
            print("\n\nYou have inserted 5 Odd numbers.\nMaximum number is : ",max(odd),"\nTotal of this list is:", sum(odd), "\nWith Avg of :", avg, "\n\nOdd List is: ")
            print(odd)
else:
    avg=sum(even)/len(even)
    print("\n\nYou have inserted 5 Even numbers.\nMaximum number is : ",max(even),"\nTotal of this list is:", sum(even), "\nWith Avg of :", avg, "\n\nEven List is: ")
    print(even)
#11
a={}
new = list(input("enter"))
for i in new:
    if i.isalpha():
        if i in a:
            a[i]+=1
        else:
            a[i]=1
print(a)

#12
a = (1,2,3,4,5,6,7,8,9,10)
new = tuple(i for i in a if i%2==0)
print(new)
