import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    phone = sorted([sys.stdin.readline().split() for _ in range(n)])
    flag = True
    for i in range(n-1): # 바로 다음꺼랑 비교
        if phone[i+1][0].startswith(phone[i][0]):
            flag = False
            break
    print("YES" if flag else "NO")



# 메모리 초과, combinations 때문이다.

