name = "cheeku"
sentence = "I live in ghaziabad"

# I evil ni dabaizahg

print(sentence)

sentence.upper()

num = [1,2,4,5]

print(num[::-1])


# reverse a string
print(name[::-1])

print(sentence[::-1])

# to get output: I evil ni dabaizahg
words = sentence.split(' ')
print(words)

res = []
for word in words:
    res.append(word[::-1])

print(res)

new_str = " ".join(res)
print(new_str)
