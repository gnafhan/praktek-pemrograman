# a = [[1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8]]
a = [0]*8
for i in range(8):
    a[i] = list(map(int, input().split()))
b =[[0]*8 for m in range(8)]
for i in range(8):
    for j in range(8):
        b[i][j] = a[7-i][7-j]
# b = [[1,2,3], [2,3,4], [4,5,6]]
# c = map(str, b)

# print(list(c))
print("output: ")
for i in range(len(b)):
    print(" ".join(map(str, b[i])))