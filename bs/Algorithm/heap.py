import heapq
def solution(x):
    nums = [1,5,4,8,7,3]
    heap = []
    for i in nums:
        # heapq.heappush(heap , (-i,i))
        heapq.heappush(heap , (-i,i))
    while heap:
        print(heapq.heappop(heap))


    #      1  ---> root 이런느낌
    #    /   \
    #   3     5
    #  / \   /
    # 4   8 7

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
# 상향식

def heap_sort(array):
    n = len(array)
    # 전체 트리 구조를 최대 힙 구조로 바꿈
    for i in range(n):
        c = i
        while c != 0:               # c는 자식노드
            r = ( c-1 ) // 2        # r은 부모노드 의 인덱스
            if (array[r] < array[c]):   # 자식이 더크면 부모와 교환
                array[r], array[c] = array[c], array[r]
            c = r               # 자식노드에서 부모노드로 이동
            # print(array)

    # 크기를 줄여가면서 heap 구성
    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]  # 첫 값과 맨 뒤에 있는 원소를 바꿈
        r = 0   # 루트의 위치
        c = 1   # 변수 이용
        while c < j:
            c = 2 * r +1    # 자식
            # 자식 중 더 큰 값 찾기
            if (c < j - 1) and (array[c] < array[ c+1 ]):
                c += 1
            # c 와 c+1 중 비교해서 더 큰값을 c 에 넣어주는 것
            # 범위를 벗어나지 않게 c<j-1 로 막아준것

            # 루트보다 자식이 크다면 교환
            if (c < j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r = c
            # 다시 c 를 r로 이동시켜 재귀적으로 동
    print(array)
heap_sort(array)