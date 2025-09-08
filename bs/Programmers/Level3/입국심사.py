def solution(n, times):

    res = 0  # 결과 변수 초기화
    left, right = 1, max(times) * n  # 범위 설정

    while left <= right:  # 이분 탐색
        mid = (left + right) // 2  # 중간 시간 설정
        people = 0  # 현재 시간(mid)까지 심사를 받은 사람의 수

        for i in times:  # 각 심사관이 심사하는 시간에 대해 반복
            people += mid // i  # 현재 시간 동안 각 심사관이 처리할 수 있는 사람의 수 계산
            if people >= n:  # 모든 사람이 심사를 받았을 경우 반복 중단
                break

        if people >= n:  # 모든 사람이 심사를 받을 수 있는 경우
            res = mid  # 현재 시간을 결과 변수에 저장
            right = mid - 1  # 최소 시간을 찾기 위해 범위를 좁힘
        else:  # 모든 사람이 심사를 받지 못하는 경우
            left = mid + 1  # 최소 시간을 찾기 위해 범위를 좁힘
    return res  # 결과 반환
print(solution(6, [7, 10]))