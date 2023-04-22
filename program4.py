# reverse a number
# 342==243

number = int(input("Enter a number: "))

def reverse(num):
    string = str(num)
    result = string[::-1]
    print(result)
    
reverse(number)


'''def reverse_num(num):
    rev_num = 0
    while(num>0):
        rem = num % 10
        num = num//10
        rev_num = rev_num*10+rem
    print(rev_num)


reverse_num(254)'''
