import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import heapq

min_heap =[] ; max_heap = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)
in_list = defaultdict(bool)
N = int(input())

for i in range(N):
    number, level = map(int,sys.stdin.readline().rstrip().split(" "))
    heapq.heappush(min_heap,(level,number))
    heapq.heappush(max_heap,(-level,-number))
    in_list[number] = True
M = int(input())
for _ in range(M):
    lst = sys.stdin.readline().rstrip().split(" ")
    # if lst[0] == "add":
    if lst[0] == "recommend":
        if lst[1] == "1":
            while not in_list[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while not in_list[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])
    elif lst[0] == "solved": # 삭제 시켜줘야하는 것은
        in_list[int(lst[1])] = False # False로 바꿔줌
    else:
        # add 일때 이미 solved로 푼 문제가 heap에서는 사라지지 않고 dict에만 False로 저장되어 출력 되는것을 방지해야한다.
        while not in_list[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not in_list[min_heap[0][1]]:
            heapq.heappop(min_heap)
        in_list[int(lst[1])] = True
        heapq.heappush(max_heap,(-int(lst[2]),-int(lst[1]))) # 난이도, 문제번호 넣어줌
        heapq.heappush(min_heap,(int(lst[2]),int(lst[1]))) # 난이도, 문제번호 넣어줌