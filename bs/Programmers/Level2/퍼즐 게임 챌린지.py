

def solution(diffs, times, limit):
    def can_solve(level):
        total_time = 0
        prev_time = 0

        for i in range(len(diffs)):
            current_time = times[i]
            # 난이도가 레벨보다 높으면 추가 시간 계산
            if diffs[i] > level:
                total_time += (diffs[i] - level) * (current_time + prev_time) + current_time
            else:
                total_time += current_time
            prev_time = current_time

        return total_time <= limit

    # 이진 탐색 설정
    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_solve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer



print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))
