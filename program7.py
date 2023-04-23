# armstrong
# 153 = 1**3 + 5**3 + 3**3 = 153
""" 
 125
  27
+  1
-----
 153
-----
"""


def armstrong(num: int):
    org = num
    length = len(str(num))
    res = 0
    while num != 0:
        rem = num % 10
        res = res + rem**length
        num = num // 10
    print(org, res, length)
    if org == res:
        print("This is an armstromg number.")
    else:
        print("This is not an armstromg number.")


armstrong(153)
