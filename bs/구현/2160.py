import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n=int(input())
pic=[]
for i in range(n):
    pic.append(list([input().rstrip() for _ in range(5)]))

a=[]
for i in range(n-1):
    for j in range(i+1,n):
        temp=0
        for k in range(5):
            for l in range(7):
                if pic[i][k][l]!=pic[j][k][l]:
                    temp+=1
        a.append((temp,i+1,j+1))

result=min(a)
print(result[1],result[2])
