import math


# def solution(n, stations, w):
#     count = 0
#     maps = [0 for _ in range(n)]  # 인덱스 오류 수정
#     for station in stations:
#         for i in range(station - w - 1, station + w):  # 인덱스 오류 수정
#             if i >= 0 and i < len(maps):  # 인덱스 오류 수정
#                 maps[i] = 1
#     result = []
#     zeros = []
#     answer = 0
#     for i, num in enumerate(maps):
#         if num == 0:
#             zeros.append(i)
#         elif len(zeros) > 0:
#             result.append(zeros)
#             zeros = []
#     if len(zeros) > 0:
#         result.append(zeros)
#     for i in range(len(result)):
#         # 연속된 범위를 고려하여 필요한 기지국의 개수 계산
#         answer += math.ceil(len(result[i]) / (2 * w + 1))
#
#     return answer

def solution(n, stations, w):
    answer = 0
    current = 1 # 현재 아파트 번호
    i = 0 # 현재 기지국 인덱스

    while current <= n:
        if i < len(stations) and current >= stations[i] - w: # 기지국 범위에 포함되는 경우
            current = stations[i] + w + 1 # 기지국 범위 바깥으로 이동
            i += 1 # 다음 기지국으로 이동
        else: # 기지국 범위에 포함되지 않는 경우
            current += w * 2 + 1 # w만큼의 범위를 커버하기 위해 기지국 설치
            answer += 1 # 기지국 설치 개수 증가

    return answer

# print(solution(16,[9],2))


print(solution(	11, [4, 11], 1))
print(solution(	16, [9], 2))