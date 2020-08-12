#1. Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
def fun(c):
    try:
        a=5
        b=6
        print("in the try block")
        d=a+b+c:
        print(d)
    except SyntaxError:
        print("in except block because of syntax error")
    finally:
        print("finally block")
c=int(input("enter something"))
fun(c)
#2. Write a program in Python to allow user to open a file by using argv module.
#If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
from sys import argv
prg , filee = argv
print("enter the program name", prg)
print("enter the file name", filee)
while True:
    try:
        filevariable=open(filee)
        data=filevariable.read()
        print(data)
        filee.close()
        break
    except:
        print("entered name is wrong.")
        again=input("would you ike to try again ? \n 'Y' for Yes \n 'N' for No")
        if again == "Y":
            filee = input("Enter the file name again")
        else:
            break
#3. Write a program to handle an error if the user entered the number more than four digits
# it should return “Please length is too short/long !!! Please provide only four digits”

a=input("Please enter the number")
for i in a:
    if i.isalpha():
        print("Only integers are allowed, not any alphabet")
        break
    if len(a) > 4 or len(a) < 4:
        raise Exception("Do not enter more or less than 4 digits, Four digits are allowed only")
else:
    print("Everything is fine with the above number:",a)
#4. Create a login page backend to ask user to enter the UserEmail and password.
#Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
    def acccheckfirst(ui, pw):  # if user ask to make a new account but if the email address is taken""
        line = open("storeduserdata.txt", "r")
        for i in range(0, 1):
            if ui in line.read():
                print("Account Name has been taken, Try Something else")
                break
        else:
            newaccfun(ui, pw)


def newaccfun(ui,
              pw):  # if the emaail address it available, user can make with after getting the email adn pass correct only
    b = list(ui)
    le = len(ui) - 5
    c = list(".com")
    xx = xxx = 0
    for i in range(-4, 0):
        if b[i] == c[i]:
            xx += 1
    for i in range(0, le):
        if b[i] == "@":
            xxx += 1
    yy = sum(map(str.isupper, pw))
    if xx == 4 and xxx == 1 and len(pw) >= 8 and yy >= 1:
        u = "\n" + ui
        p = " -- " + pw
        f = open("storeduserdata.txt", "a")
        f.write(u + p)
        f.close()
        print("New Account has been Created with username: ", ui)
    else:
        print("Provided Information is unappropriate")


def exiaccfun(ui, pw):  # for the existing account
    lines = open("storeduserdata.txt", "r")
    for i in range(0, 1):
        if ui in lines.read():
            sd = input(
                "welcome to the account\npress 1 to Store data in your file\npress 2 to read data from your file\npress 3 for exit\n")
            if sd == "1":
                print("have to work fto append the data")
            elif sd == "2":
                print("have to work to read the data")
            elif sd == "3":
                print("exit")
            else:
                print("this credential does not belong to any account")
                break


inp = input("First time User Press 1\nExisting User Please press 2  \n")
if inp == "1":
    print(
        "\nTo Creat New Account please enter your details\n\n************\nEmail address should be in formate\nPassword should contain One or more upper letters\nPassword should be longer than 8\n************\n")
    ui = input("Enter the Email-ID : ")
    pw = input("Enter the Password : ")
    acccheckfirst(ui, pw)
elif inp == "2":
    ui = input("Enter the Email ID : ")
    pw = input("Enter the Password : ")
    apw = input("Enter the Password again : ")
    c = 0
    t = 3
    while c < 3 and pw != apw:
        print(t, "Trials Left")
        apw = input("password doesnot match, Please enter password again: ")
        c += 1
        t -= 1
    if pw == apw:
        print(1)
        exiaccfun(ui, pw)

else:
    print("Entry is invalid")

#5. https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.
'''Raise is used to generate defined exception according to requirement and function.
Finally is the block whch can have the must run program in it after try and exception blocl, 
which will definitely run for sure, we can use that for counting of total loop and that kind of nexxesary fuctions, 
which has to run all the time in program in any situation.'''


#6. Read any file using Python File handling concept and return only the even length string from the doc.txt file.
#Consider the content as:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in
#The same link as it is present.
try:
    b=open("data.txt","r")
    for i in b:
        if len(i)%2==0:
            print (i, "length ->" ,len (i))
finally:
    b.close() 
