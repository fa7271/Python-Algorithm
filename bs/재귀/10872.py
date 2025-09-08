import sys
sys.stdin = open('/Python/h.txt', 'r')

N = int(input())
list = list()
a= 1
for i in range(1,N+1):
    list.append(a)
    a +=1

result = 1

for i in range(1,len(list)+1):
    result *= i

print(result)