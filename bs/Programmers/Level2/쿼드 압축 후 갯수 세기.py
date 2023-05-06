


def check(x, y, n, arr):
    # 탈출 조건
    if n == 1:
        if arr[x][y] == 1:
            return [0, 1] # 1 카운트 증가
        else:
            return[1, 0] # 0카운트 증가
    left_up = check(x, y, n//2, arr) # 2사분면 체크
    right_up = check(x, y+n//2, n//2, arr) # 1사분면 체크
    left_down = check(x+n//2, y, n//2, arr) # 3사분면 체크
    right_down = check(x+n//2, y+n//2, n//2, arr) #4사분면 체크

    # 각 축소 후 압축할지 여부 결정

    if left_up == right_up == left_down == right_down ==[0,1] or left_up == right_up == left_down == right_down == [1,0]:
        return left_up # 4개가 같은 숫자면 1개로 리턴
    else:
        return list(map(sum, zip(left_up, right_up, left_down, right_down)))


def solution(arr):
    answer = check(0, 0, len(arr), arr)
    return answer

print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
