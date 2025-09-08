import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
input = sys.stdin.readline

def find_number(start, end):
    while start <= end:
        mid = (start + end) // 2
        res = 0
        for i in arr:
            if i > mid:
                res += mid
            else:
                res += i
        if res <= m: # 총예산보다 크면 줄이면 된다.
            start = mid + 1
        else:
            end= mid -1
    return end

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
a = find_number(0, max(arr))
print(a)

