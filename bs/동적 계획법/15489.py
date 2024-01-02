import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def solution(scovilles, K):
    scovilles.sort()
    scoville = deque(scovilles)
    count = 0

    while scoville[0] < K:
        left, right = scoville[0], scoville[1]

        # del scoville[0]
        # del scoville[0]

        scoville.popleft()
        scoville.popleft()

        new_node = left + (right * 2)

        insert_value(scoville, new_node)
        count += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return count


def insert_value(lst, value):
    # 이분 탐색을
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < value:
            left = mid + 1
        else:
            right = mid
    lst.insert(left, value)


print(solution([1, 3, 2, 9, 10, 12], 7))

# int x = Q.get(0);
# int y = Q.get(1);
# Q.remove(0);
# Q.remove(0);
# Q.add(x + y*2);
# Collections.sort(Q);
# System.out.println("Q = " + Q);
#
# count ++;
# if (Q.size() == 1 && Q.get(0) < K) {
# }
# return count;
