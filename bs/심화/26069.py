import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(sys.stdin.readline())
sets =set()
sets.add("ChongChong")
for i in range(n):
    left, right = sys.stdin.readline().rstrip().split(" ")
    if left in sets :
        sets.add(right)
    elif right in sets:
        sets.add(left)
print(len(sets))