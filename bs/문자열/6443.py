import sys
from collections import defaultdict
from itertools import permutations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

def bt(count):

    # 길이만큼 만들면
    if count == len(word):
        # 정답 프린트 해주고
        print("".join(res))
        # 리턴
        return
    # dic 돌면서
    for i in dic:
        if dic[i]:
            # 사용 했으니깐 1 빼주고
            dic[i] -= 1
            # i 를 단어에 추가 해줌
            res.append(i)
            # 다음 재귀 출발
            bt(count+1)
            # 돌아오면 다시 복구 사용 안 한것 처럼 해줘야함
            dic[i] += 1
            # res에 넣은것도 당연히 빼줘야함
            res.pop()
    return

for _ in range(n):
    word = sorted(list(map(str, sys.stdin.readline().strip())))
    res = []
    dic = defaultdict(int)
    for w in word:
        dic[w] += 1
    # 반복문을 통해 visited에 알파벳의 개수를 입력
    bt(0)

