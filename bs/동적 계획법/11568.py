import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


T = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split(" ")))
"""
O(N^2)
dp = [1 for i in range(T+1)]
# 최장 증가수열
for i in range(T):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
"""



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:    # 중간값이 타겟보다 크거나 같으면 오른쪽 범위를 줄임
            right = mid - 1
        else:   # 중간값이 타겟보다 작으면 왼쪽 범위를 줄임
            left = mid + 1
    print("return : ", left)
    return left

lis = []   # 최장 증가 수열 리스트

for num in lst:   # 입력으로 주어진 수열을 순회
    idx = binary_search(lis, num)   # 현재 숫자를 삽입할 인덱스를 이진 탐색으로 찾음
    if idx == len(lis):   # 인덱스가 lis의 길이와 같다면 해당 숫자를 lis에 추가 즉 lis에 있는 값보다 크
        lis.append(num)
    else:   # 인덱스가 lis의 길이보다 작다면 해당 인덱스에 숫자를 바꿔줌
        lis[idx] = num

print(len(lis))
