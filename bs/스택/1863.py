import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())  # 건물의 개수 입력
#
# lst = [int(sys.stdin.readline().split()[1]) for i in range(n)]  # 건물의 높이를 리스트에 저장
# lst.append(0)  # 스택 연산을 위한 초기 설정: 높이가 0인 가상의 건물 추가
#
# stk = [0]  # 높이를 저장하는 스택 초기화
# res = 0  # 도시에 세워진 건물의 개수 초기화
#
# for i in lst:  # 건물 리스트 순회
#     now = i  # 현재 건물의 높이
#
#     while stk[-1] > i:  # 스택의 마지막 원소가 현재 높이보다 큰 경우 반복
#         if stk[-1] != now:  # 스택의 마지막 원소가 이전 건물의 높이와 다른 경우
#             res += 1  # 새로운 건물의 시작을 의미하므로 건물 개수 증가
#             now = stk[-1]  # 현재 건물의 높이를 스택의 마지막 원소로 갱신
#         stk.pop()  # 스택의 마지막 원소 제거
#
#     stk.append(i)  # 현재 건물의 높이를 스택에 추가
#
# print(res)  # 도시에 세워진 건물의 개수 출력

stack = []  # 건물의 높이를 저장하는 스택
cnt = 0  # 도시에 세워진 건물의 개수

for i in range(n):  # 건물의 개수만큼 반복
    nums = list(map(int, input().split()))  # 건물의 번호와 높이 입력 받음
    print(stack,cnt)
    while stack:  # 스택이 비어있지 않은 동안 반복
        if stack[-1] > nums[1]:  # 스택의 마지막 원소가 현재 건물의 높이보다 큰 경우
            cnt += 1  # 새로운 건물의 시작을 의미하므로 건물 개수 증가
            stack.pop()  # 스택의 마지막 원소 제거
        elif stack[-1] == nums[1]:  # 스택의 마지막 원소가 현재 건물의 높이와 같은 경우
            stack.pop()  # 스택의 마지막 원소 제거
        else:
            break  # 스택의 마지막 원소가 현재 건물의 높이보다 작은 경우 반복 중단

    stack.append(nums[1])  # 현재 건물의 높이를 스택에 추가
while stack:  # 스택에 남아있는 건물들을 처리
    new = stack.pop()
    if new >= 1:  # 높이가 1 이상인 경우
        cnt += 1  # 건물 개수 증가

print(cnt)  # 도시에 세워진 건물의 개수 출력