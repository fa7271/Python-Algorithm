import collections
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
t = int(input())

for i in range(t):
    W = input()
    K = int(input())
    alpha = collections.defaultdict(list)
    for i in range(len(W)):
        if W.count(W[i]) >= K:
            alpha[W[i]].append(i)
    min_res = 10001; max_res = -1

    # 알파벳 인덱스
    for i in alpha.values():
        # 만약 2개씩 짤랐을때 3개면 2개고 2개면 1개이기 때문에 조건 을 len(i) - k + 1
        for j in range(len(i)-K+1):
            # k개 포함하는 범위의 길이
            res = i[j+K-1] - i[j] + 1
            min_res = min(min_res,res)
            max_res = max(max_res,res)
    if not alpha:
        print(-1)
    else:
        print(min_res,max_res)

# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
