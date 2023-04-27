# find max and min value from array

num = [2, 1, 7, 15, 9, 3, 8, 22]
min = max = None

for i in num:
    if min == None:
        min = i
    if max == None:
        max = i
    if i > max:
        max = i
    if i < min:
        min = i
print(max,min)