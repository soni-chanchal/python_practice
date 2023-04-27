# Linear search

num = [24, 536, 6464, 664, 2, 24, 55, 77, 4]

number = int(input("Enter a number to be search: "))

for i in num:
    if i == number:
        print("Element is present in array")
        break
else:
    print("not in array")
    