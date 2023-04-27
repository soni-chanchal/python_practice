# fibonacci
# 0 1 1 2 3 5 8 13 21 34 55

number = int(input('Enter number of terms you want to print: '))

def fibonacci(num: int):
    a = 0
    b = 1
    if num < 0:
        print("Enter a valid number")
    elif num == 0:
        print(a)
    elif num == 1:
        print(a,b, end =' ')
    else:
        print(a, end= ' ')
        for i in range(1,num):
            b = a+b
            print(b, end = ' ')
            a,b = b,a

fibonacci(num=number)

