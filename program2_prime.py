# prime number

number = int(input("Enter a number: "))

def check_prime(num):
    if num < 1:
        print("Enter a valid number")
    elif num == 2:
        print("This is only a even prime number")
    else:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                print("This is not a prime number")
                is_prime = False
                break
        if is_prime:
            print("This is a prime number")

check_prime(number)
        
