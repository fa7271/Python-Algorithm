import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

res = 0


def bt(Node):
    global res
    if Node == N:
        total = 0
        for i in range(N):
            if lst[i][0] <= 0:
                total += 1
        res = max(res, total)
        return
    # 현재 손에 든 계란이 깨짐
    if lst[Node][0] <= 0:
        bt(Node+1)
    #안 깨진 경우asd
    else:
        # 부셨는지 여부 체크
        flag = False
        for i in range(len(lst)):
            if i == Node or lst[i][0] <= 0:
                continue  # 자기자신 x, 깨진경우 못 부시니깐 넘어감.
            flag = True
            lst[Node][0] -= lst[i][1]
            lst[i][0] -= lst[Node][1]

            bt(Node + 1)

            lst[Node][0] += lst[i][1]
            lst[i][0] += lst[Node][1]
        # 자기자신이거나, 깨진경우이면 다음 노드로 넘어감
        if flag == False:
            bt(Node+1)
bt(0)
print(res)
