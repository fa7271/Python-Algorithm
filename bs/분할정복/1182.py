import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, S = map(int,sys.stdin.readline().rstrip().split(" "))
arr = list(map(int,sys.stdin.readline().rstrip().split(" ")))
cnt = 0
res = 0
# def solution(idx):
#     global cnt
#     if sum(res) == S and len(res) > 0:
#         cnt += 1
#
#     for i in range(idx,N):
#         res.append(arr[i])
#         solution(i+1)
#         res.pop()
#
# solution(0)
# print(cnt)

# def solution(num,sum):
#     global cnt
#     if num == N:
#         return
#     sum += arr[num]
#     if sum == S:
#         cnt += 1
#
#     solution(num+1,sum)
#     solution(num+1,sum-arr[num])
#
# solution(0,0)
# print(cnt)



def solution(num, total):
    global cnt,res
    if num == N:
        if total == S:
            cnt += 1
        return

    res += arr[num]
    solution(num+1, res)
    res -= arr[num]
    solution(num+1, res)

solution(0, 0)
print(cnt)