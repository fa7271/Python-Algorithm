
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def can_find_subset(A, K):
    from collections import defaultdict

    if K > len(A):
        return False

    count = defaultdict(int)
    required_cards = set(range(1, K + 1))
    found_cards = set()

    l = 0
    for r in range(len(A)):
        if 1 <= A[r] <= K:
            count[A[r]] += 1
            found_cards.add(A[r])

        if r - l + 1 > K:
            if 1 <= A[l] <= K:
                count[A[l]] -= 1
                if count[A[l]] == 0:
                    found_cards.remove(A[l])
            l += 1

        if r - l + 1 == K and found_cards == required_cards:
            return True

    return False

def find_max_K(A):
    left, right = 1, len(A)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_find_subset(A, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# 결과 출력
print(find_max_K(A))
