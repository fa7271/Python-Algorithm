import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



def merge_sort(start, end):
    global result
    if end - start < 1:
        return

    mid = int(start + (end - start) / 2)
    # 재귀 함수
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    # 임시 저장 배열
    for i in range(start, end + 1):
        temp_list[i] = array[i]
    #     합병
    k, x, y = start, start, mid + 1
    while x <= mid and y <= end:
        # 뒤쪽 배열의 앞에 값이 더작음 그러면 앞에 크기만큼 더해줘야함
        if temp_list[x] > temp_list[y]:
            array[k] = temp_list[y]
            result = result + y - k
            # 시작값 올리고
            k += 1
            # 뒤에 값 올림
            y += 1
        else:
            array[k] = temp_list[x]
            k += 1
            x += 1
    while x <= mid:
        array[k] = temp_list[x]
        k += 1
        x += 1
    while y <= end:
        array[k] = temp_list[y]
        k += 1
        y += 1

N = int(input())
array = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))
temp_list = [0] * (N + 1)
result = 0

merge_sort(1, N)
print(result)
print(array,temp_list)