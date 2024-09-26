import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N, K = map(int, input().split())
numbers = [0] * 1000001
end = 0
for _ in range(N):
    a, b = map(int, input().split())
    numbers[b] = a
    end = max(end, b)
step = 2 * K + 1
window = sum(numbers[:step])
res = window
for i in range(step, end+1):
    window += numbers[i] - numbers[i-step]
    res = max(res, window)
print(res)



