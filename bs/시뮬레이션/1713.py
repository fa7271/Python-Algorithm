import sys
from collections import deque,Counter
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())  # 사진틀의 개수
R = int(sys.stdin.readline())  # 전체 학생의 추천 횟수
lst = list(map(int, sys.stdin.readline().split()))  # 전체 학생의 추천 결과

stk = deque()  # 사진틀을 저장할 덱
counts = Counter()  # 학생별 추천 횟수를 저장할 Counter 객체

for student in lst:
    if student in stk:  # 이미 사진틀에 게시된 경우
        counts[student] += 1  # 해당 학생의 추천 횟수 증가
    elif len(stk) < N:  # 사진틀에 자리가 있는 경우
        stk.append(student)  # 사진틀에 추가
        counts[student] += 1  # 해당 학생의 추천 횟수 증가
    else:  # 사진틀이 가득 찬 경우
        min_count = min(counts.values())  # 현재까지 추천 받은 횟수가 가장 적은 학생의 추천 횟수
        min_candidates = [s for s in stk if counts[s] == min_count]  # 추천 횟수가 가장 적은 후보들
        remove_student = min(min_candidates, key=lambda x: stk.index(x))  # 가장 오래된 후보를 선택
        stk.remove(remove_student)  # 가장 오래된 후보 삭제
        stk.append(student)  # 새로운 학생의 사진 게시
        counts[student] += 1  # 해당 학생의 추천 횟수 증가

result = sorted(stk)  # 사진틀에 남아있는 후보들을 학생 번호 순으로 정렬
print(*result)



N = int(input())
W = int(input())
num = list(map(int, input().split(" ")))

photo = dict()
for i in range(W) :
    if num[i] in photo : # 숫자가 있으면
        photo[num[i]][0] += 1 # 추천수 증가시켜주고
    else : # 숫자가 없으면
        if len(photo) < N : # 액자 크기 확인해서 자리가 있으면
            photo[num[i]] = [1, i] # 추천수1 과, 들어온 순서를 넣어준다.
        else: # 액자가 꽉 찼으면 1. 가장적은사람  2.가장 오래된사람 으로 정렬
            x = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]) ) # 추천수, 오래 된 사람.
            x = x[0][0] # 지워야 하는 사람 추천수도 낮고 오래된 사람
            del photo[x] # 지워주고
            photo[num[i]] = [1, i] # 추천수1 과, 들어온 순서를 넣어준다.
lst = sorted(photo.keys())
print(*lst)

