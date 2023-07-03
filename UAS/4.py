x = list(input().split(' '))
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)