import sys
sys.stdin = open('/Python/h.txt', 'r')


# 버블 정렬의 범용성을 높이기 위해 함수로 만듬
# 가장 일반적인 퀵 정렬
def quick_sort(array, start, end):
    if start >= end: return # 원소가 1개인 경우
    pivot = start # 피벗은 첫 요소
    left, right = start + 1, end
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

array = [10,9,8,7,6,5,4,3,2,1]
quick_sort(array,0,len(array)-1)
print(array)