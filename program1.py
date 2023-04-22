# take input from user and check it is even or odd...

number = int(input("Enter a number: "))
 
def check_even(num):
    if num % 2 == 0:
        print("This is a even number")
    else:
        print("This is a odd number")

check_even(number)