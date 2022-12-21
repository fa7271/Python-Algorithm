def check(x, y, n, arr):
    if n == 1:
        if arr[x][y] == 1:
            return [0, 1]
        else:
            return [1, 0]
    left_up = check(x, y , n // 2, arr)
    right_up = check(x, y + n // 2, n // 2, arr)
    left_down = check(x + n // 2, y, n // 2, arr)
    right_down = check(x + n // 2, y + n // 2, n // 2, arr)

    if left_up == right_up == left_down == right_down == [0, 1] or left_up == right_up == left_down == right_down == [1, 0]:
        return left_up
    else:
        print(list(map(sum, zip(left_up, right_up, left_down, right_down))))
        return list(map(sum, zip(left_up, right_up, left_down, right_down)))

def solution(arr):
    answer = check(0,0,len(arr), arr)
    return answer
print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
# print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]])) # 15
