a = input()
b = input()

valueA = 0
valueB = 0

if len(a) == len(b):
    for i in range(len(a)):
        valueA += ord(a[i])
        valueB += ord(b[i])
    if valueA == valueB:
        print("anagram")
    else:
        print("bukan anagram")
else:
    print("bukan anagram")
