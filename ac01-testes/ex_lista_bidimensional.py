x = 3
s = 1
v = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for j in range(x):
    for i in range(x):
        v[i][j] = v[i][j] * 2
        if v[i][j] == i:
            s = s + v[i][j]
print(s)