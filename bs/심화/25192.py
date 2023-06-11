import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(sys.stdin.readline().rstrip())

sets = set()
count = 0

for i in range(n):
    name = input()

    if name == "ENTER":
        count += len(sets)
        sets.clear()
    else:
        sets.add(name)
count += len(sets)
print(count)

# sets.remove("ENTER")
# print(sets)