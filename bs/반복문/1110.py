import sys
sys.stdin = open('/Python/h.txt', 'r')

a = b = int(input())
count =0
print(a,b)
while True:
    ten = a//10
    one = a%10
    total = ten + one
    count += 1
    a =int(str(a%10)+str(total%10))
    if(a == b):
        break
print(count)
