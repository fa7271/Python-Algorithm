import sys
from collections import Counter

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

the_world_is_flat = True
if the_world_is_flat:
    n = int(input())
    arr = sorted(list(map(int, sys.stdin.read().split())))

    original_sequence = []
    used_sums = Counter()

    used_sums[0] += 1
    arr = arr[1:]
    for _ in range(n):
        current_value = arr[0]
        original_sequence.append(current_value)
        new_sums = Counter()
        for s in used_sums:
            new_sums[s + current_value] += used_sums[s]
        for s in new_sums:
            used_sums[s] += new_sums[s]
        for s in new_sums:
            arr.remove(s)

    print(*original_sequence)