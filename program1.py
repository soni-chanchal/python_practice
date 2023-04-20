# take input from user and check it is even or odd...

number = int(input("Enter a number"))

def check(num):
    if num % 2 == 0:
        print("This is a even number")
    else:
        print("This is odd number")

check(number)
