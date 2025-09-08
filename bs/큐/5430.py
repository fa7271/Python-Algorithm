import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())

for i in range(T):
    func = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline().rstrip())
    lst = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    reverse_count = 0 # 짝수이면 왼쪽에서 홀수이면 오른쪽에서 pop
    if num == 0:
        lst = []
    for str in func:
        if str =="R":
            reverse_count += 1
        else:
            if len(lst) == 0:
                print("error")
                break
            else:
                if reverse_count % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
    else:
        if reverse_count % 2 == 0:
            print("[" + ",".join(lst) + "]")
        else:
            lst.reverse()
            print("[" + ",".join(lst) + "]")

