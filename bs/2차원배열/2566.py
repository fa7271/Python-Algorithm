import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst = []

for i in range(9):
    lst.append(list(map(int,input().split())))
print(lst)
max = lst[0][0]
x = 1
y = 1
for i in range(9):
    for j in range(9):
        if lst[i][j] > max:
            max = lst[i][j]
            x = i+1
            y = j+1
print(max)
print(x,y)


