import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())
board = [True] * (2000001)
board[1] = False
m = int(2000000)
lst = []
for i in range(2,m+1):
    if board[i]:
        lst.append(i)
        for j in range(i*2,m+1,i):
            board[j] = False

def check(num):
    try:
        if board[num]:
            return True
        else:
            return False
    except:
        for i in lst:
            if num % i == 0:
                return False
        return True

for i in range(T):
    S = sum(map(int,sys.stdin.readline().rstrip().split()))
    if S < 4:
        print("NO")
    elif S % 2 == 0:
        print("YES")
    else:
        if check(S-2):
            print("YES")
        else:
            print("NO")

