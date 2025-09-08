import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


list_x = []
list_y = []
for i in range(3):
    x,y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
print(list_x)
for i in range(3):
    if list_x.count(list_x[i]) == 1:
        x = list_x[i]
    if list_y.count(list_y[i]) == 1:
        y = list_y[i]

print(x,y)


