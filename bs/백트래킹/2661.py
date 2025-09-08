import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())

def bt(res,cnt):
    for i in range(1, cnt//2+1):
        if str(res)[-i:] == str(res)[-i*2:-i]:
            return
    if cnt == N:
        print(res)
        exit(0)
    for i in range(1,4):
        tmp = (res*10) +i
        bt(tmp,cnt+1)

print(bt(0,0))