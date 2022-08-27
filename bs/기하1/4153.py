import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())
#
# list_x = []
# list_y = []
# list_z = []
# for i in range(3):
#     x,y,z = map(int,input().split())
#     list_x.append(x**2)
#     list_y.append(y**2)
#     list_z.append(z**2)
#
# for i in range(len(sys.stdin.readline())-1):
#     if list_z[i] == list_x[i] + list_y[i]:
#         print('right')
#     else:
#         print('wrong')
#
# print(0,0,0,sep= " ")


li = []

while True:
    a = list(map(int,input().split()))
    if(a == [0, 0, 0]):
        break
    li.append(a)

for i in li:
    i.sort()
    if(i[0]**2 + i[1]**2 == i[2]**2):
        print("right")
    else:
        print("wrong")