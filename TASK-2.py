#TASK-2(4)
#Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”

while True:
    x = eval(input('Enter a number'))
    y = x

    if (y+x==0) or (y+x<0):
        print("it's over")
        break
    else:
        print('good going')
        continue

#TASK-2(5)
#Write a program in Python which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200.

l=[]
count=0
for x in range(2000,3201):
    count+=1
    if (x%7==0) and (x%5!=0):
        l.append(x)
print(l)
print('Total number of result ==',count)

#TASK-2(6)
#What is the output of the following code examples?
x=123
for i in x:
    print(i)
#ERROR and the sollution is,you can select list itself or range for using for loop

############################################################################################
i=0
while i<5:
    print(i)
    i += 1
    if i==3:
        break
    else:
        print('ERROR')
#0
#ERROR
#1
#ERROR
#2

#########################################################################
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
#NameError if used 'break',normal execution 0,1,2,3,4 without exception

################################################################################
#TASK-2(7)
#Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')

#TASK-2(8)
#Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#Expected output: consul12
#Letters 6
#Digits 2

x = input("ENTER A STRING TO COUNT ALPHA NUMERICS")
a=b=0
for c in x:
    if c.isdigit():
        a=a+1
    elif c.isalpha():
        b=b+1
    else:
        pass
print("Total Letters =", a)
print("Total Digits =", b)

#TASK-2(9)
#Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
#●Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the
# answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”.
# ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
while True:
    x=int(input('Guess the lucky number'))
    if x!=7:
        print('Please try again')
    else:
        print('GOOD GUESS !!!')
        break
#modified

number=895648
answer=''

while True:
    number=int(input('Guess the number'))
    if number==7:
        break
    else:
        answer=input('Do you want to continue?')
        if answer == 'yes':
            continue
        else:
            break

#TASK-2(10)
y = 7
counter = 1

while counter <=5:
    print('Type in the', counter, 'number')
    x= int(input("Guess  Lucky number "))
    if x == y:
        counter+=1
        print('Good Guess')
    elif counter ==5:
        print("Game Over")
        break
    else :
        print('Try again')
        counter+=1
        continue

#TASK-2(11)
x = 7
counter = 1

while counter <=5:
    print('Type in the', counter, 'number')
    y= int(input("Guess Lucky number "))
    if y == x:
        print('GOOD MATCH')
        break
    elif counter ==5:
        print("Game Over")
        break
    else :
        print('Try again')
        counter+=1
        continue