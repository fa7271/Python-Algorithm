import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())


def dp(num):
    z = [1, 0, 1]
    o = [0, 1, 1]
    for i in range(3,num+1):
        z.append(z[i-1] + z[i-2])
        o.append(o[i-1] + o[i-2])
    print(z[num],o[num])


for i in range(T):
    num = int(sys.stdin.readline().rstrip())
    dp(num)


# 풀이 2
z = [1, 0, 1]
o = [0, 1, 1]
def dp(num):
    if len(z) <= num:
        for i in range(len(z),num+1):
            z.append(z[i-1] + z[i-2])
            o.append(o[i-1] + o[i-2])
    print(z[num],o[num])


for i in range(T):
    num = int(sys.stdin.readline().rstrip())
    dp(num)