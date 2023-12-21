import sys
from collections import defaultdict
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import sys
#돌았냐고
n = int(input())
target_name = input()
word_list = [input() for _ in range(n)]

count = 0
def check(word):

    for s_idx, s_word in enumerate(word):
        if s_word == target_name[0]: # 시작 찾아 버림
            for e_idx, e_word in enumerate(word[s_idx:], start=s_idx):
                if e_word == target_name[-1]: # 마지막 인덱스 찾음
                    avg = (e_idx - s_idx) // (len(target_name) - 1) # 평균 간격을 재서 그 안에 데이터 들이 들어가있으면 만들 수 있음.
                    if all(word[s_idx + (avg * count)] == target_name[count] for count in range(len(target_name))):
                        return 1
    return 0

for word in word_list:
    count += check(word)
print(count)


# # 시간 초과
# for _ in range(n):
#     word = list(enumerate(input(), start=1))
#     word_list = combinations(word, len(target_word))
#     for i in word_list:
#         res = ""  # 문자담기
#         idx = []  # 문자있는 위치 담기
#         for j in i:
#             res += j[1]  # 문자추가
#             idx.append(j[0])  # 문자 인덱스 추가
#         if res == target_word:  # 문자가 정답이랑 같으면
#             diff = []  # 문자 인덱스들 차이 넣어야함
#             for k in range(1, len(idx)):  # 1,2,3
#                 diff.append(idx[k] - idx[k - 1])
#             if len(set(diff)) == 1:
#                 count += 1
#                 break
#             # 차이 확인
# print(count)



