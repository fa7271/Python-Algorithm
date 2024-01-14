from collections import deque


def solution(stones, k):
    result = deque()
    answer = []

    # 슬라이딩 윈도우 최솟값 저장
    for idx in range(len(stones)):
        # 처음과 마지막 인덱스 값이 k개 이하 여야함
        if result and result[0][0] <= idx - k:
            result.popleft()

        while len(result) >= 1 and stones[idx] > result[-1][-1]:
            result.pop()
        result.append((idx, stones[idx]))
        answer.append(result[0][1])

    return min(answer[k-1::])

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

"""
슬라이딩 윈도우
stones 배열 크기 1~200,000
stones 배열 값 1 ~ 200,000,000

k 구간에 최댓값 중에 최솟값 
"""


""" 
이분 탐색 아이디어
건널 수 있는 사람의 수가 mid가 된다.
"""