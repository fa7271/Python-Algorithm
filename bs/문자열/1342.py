import sys
from collections import Counter

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def bt(temp,x):
    answer = 0
    # 길이를 다 채우면
    if x == len(N):
        # 성공하면 1 더해줌
        return 1

    for i in cnt.keys():
        # 이전 단어랑 같거나, 해당문자의 밸류값이 0 일때 (남은 글자 없으면 다음으로 넘어감)
        if i == temp or cnt[i] == 0:
            continue
        # 해당 문자 하나 빼고
        cnt[i] -= 1
        # 백트래킹
        answer += bt(i, x+1)
        # 돌아와서 문자 뺀거 다시 넣어줌
        cnt[i] += 1

    return answer


N = list(map(str, sys.stdin.readline().strip()))
cnt = Counter(N)
print(bt("",0))


