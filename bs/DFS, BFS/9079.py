import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
move = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def flip(change_arr, new_arr):
    for i in change_arr:
        new_arr[i] = '0' if new_arr[i] == '1' else '1'
    return new_arr


def bfs(numbers):
    visited = [False] * 512
    visited[int(''.join(numbers), 2)] = True

    Q = deque([(int(''.join(numbers), 2), 0)])
    while Q:
        n_num, count = Q.popleft()
        if n_num == 0 or n_num == 511:
            return count

        for number in move:
            n_numbers = flip(number, list(bin(n_num)[2:].zfill(9)))
            n_num_bin = int(''.join(n_numbers), 2)
            if not visited[n_num_bin]:
                visited[n_num_bin] = True
                Q.append((int(''.join(n_numbers), 2), count + 1))

    return -1


for _ in range(t):
    numbers = ("".join(sum([list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(3)], []))
               .replace("H", "1")
               .replace("T", "0"))
    print(bfs(numbers))
