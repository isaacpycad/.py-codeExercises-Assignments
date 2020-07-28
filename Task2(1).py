#while is used only to provide attempts for atleast 5 times

print("Enter a number to check whether it's divisible by 3 or 5 or by both")
i=0
while i<5:
    x = eval(input('Enter Your Number'))
    if x%3==0 and x%5==0:
        print('Divisible by both 3 & 5')
    elif x%3==0:
        print('Divisible by 3')
    elif x%5==0:
        print('Divisible by 5')
    i+=1
print('Max Tries Reached ....Bye!!!')
