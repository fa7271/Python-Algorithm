import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

for _ in range(n):
    start, target = map(int, sys.stdin.readline().rstrip().split(" "))
    visited = [False] * 10001
    Q = deque([(start, "")])
    while Q:
        number, word = Q.popleft()
        visited[number] = True
        if number == target:
            print(word)
        num = (2 * number) % 10000
        if not visited[num]:
            Q.append((num, word + "D"))
            visited[num] = True

        num = (n - 1) % 10000
        if not visited[num]:
            Q.append((num, word + "S"))
            visited[num] = True

        num = number // 1000 + (number % 1000) * 10
        if not visited[num]:
            Q.append((num, word + "L"))
            visited[num] = True

        num = number // 10 + (number % 10) * 1000
        if not visited[num]:
            Q.append((num, word+"R"))
            visited[num] = True
