import sys
import math
sys.stdin = open('/Python/h.txt', 'r')

a,b,v = map(int,(input().split()))
print(math.ceil((v-a)/(a-b))+1)   # math.ceil 올림함수



A, B, V = map(int, input().split())

high = V - A                        #높이
if high % (A-B) == 0:               #0으로 떨어지면 하루 더 안보내되됨
    first = int(high/(A-B))
else:
    first = int(high/(A-B) + 1)     # 0으로 안떨어지면
print(first + 1)                    # 하루 더해줘야함