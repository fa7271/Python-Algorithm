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
    res, now, idx = 0, 1, 0 # 정답값, 현재 아파트 번호, 기지국 인덱스

    while now <= n:
        # 기지국 범위 안에 포함되는 경우이다. 1, 4 - 1
        if idx < len(stations) and now >= stations[idx] - w:
            now = stations[idx] + w + 1 #아파트 번호는 기지국 바로 옆으로 이동
            idx += 1 #다음 기지국으로 이동
        else: # 포함이 안된경우 기지국 설치
            now += w * 2 +1
            res += 1
    return res

# print(solution(16,[9],2))


print(solution(	11, [4, 11], 1))
print(solution(	16, [9], 2))