import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst = sorted(list(map(int,sys.stdin.readline().split(" "))))
start = lst[2]

while True:
    count = sum([1 for i in lst if start % i == 0])
    if count >= 3:
        break
    else: start += 1
print(start)
