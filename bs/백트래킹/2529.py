import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
in_sign = list(input().split())
visited = [0] * 10
#
# res_max = ""
# res_min = ""
# for ans in [[_ for _ in range(9, 9 - n - 1, -1)], [_ for _ in range(n + 1)]]:
#     is_ans = False
#     while not is_ans:
#         print(*ans)
#         is_ans = True
#         for i in range(n):
#             if in_sign[i] == ">":
#                 if ans[i] < ans[i + 1]:
#                     ans[i], ans[i + 1] = ans[i + 1], ans[i]
#                     is_ans = False
#             else:  # <
#                 if ans[i] > ans[i + 1]:
#                     ans[i], ans[i + 1] = ans[i + 1], ans[i]
#                     is_ans = False
#     print(*ans, sep="")


def compare_number(left, right, sign):
    if sign == "<":
        return left < right
    else:
        return left > right


def bt(idx, result):
    global res_min, res_max

    if idx == n + 1: # 부틍호가 n개 일때 n+1개의 숫자가 생김. >> idx 10 이면 부등호 9 개 다 쓴겨
        if len(res_min) == 0: # 맨 처음 도착하는 백트래킹 최솟값
            res_min = result
        else:
            res_max = result
        return
    for i in range(10):  # 숫자들
        if not visited[i]:  # 방문 안 했으면
            if (idx == 0 or compare_number(result[-1], str(i), in_sign[idx - 1])): # 첫 값은 바로가야함, 다음 값 부터 부등호 체크
                visited[i] = True
                bt(idx + 1, result + str(i))
                visited[i] = False


# bt(0, "")
# print(res_max)
# print(res_min)
