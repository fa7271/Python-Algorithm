import sys
sys.stdin = open('/Python/h.txt', 'r')


# 버블 정렬의 범용성을 높이기 위해 함수로 만듬
def bubble_Sort(arr):
    n = len(arr) # 배열의 크기

    for i in range(n):
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):

            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

arr = [10,20,40,30,22,64,32,77,24,29]

bubble_Sort(arr)

for i in range(len(arr)):
    print("%d " %arr[i],end = "")