#isaac
print(   """For add-1
         for subtraction 2
         for division 3
         for mul 4
         for avg 5""")
x=int(input('Enter number from above menu for Operation::'))

def oper(x):
    if x==1:
        a, b = [eval(x) for x in input('enter two numbers for addition separated by Comma').split(',')]
        print('a+b is = ',a+b)
    elif x==2:
        a, b = [eval(x) for x in input('enter two numbers for subtraction separated by Comma').split(',')]
        if a<b:
            print('result is negative Zsa : a<b ::',a-b)
        else:
            print('a-b is = ',a-b)
    elif x==3:
        a, b = [eval(x) for x in input('enter two numbers for division separated by Comma').split(',')]
        print('a/b is = ',a/b)
    elif x==4:
        a, b = [eval(x) for x in input('enter two numbers for mul separated by Comma').split(',')]
        print('a*b is = ',a*b)
    elif x==5:
        a, b,c,d,e = [eval(x) for x in input('enter five numbers for avg separated by Comma').split(',')]
        print('AVG IS',(a+b+c+d+e)/5)
oper(x)
