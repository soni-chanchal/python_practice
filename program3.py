# program for factorial....
# 5=5 4 3 2 1=120

num = int(input("Enter a number: "))

def fact(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    print(fact)

fact(num)