import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(input())

for _ in range(T):
    left, right = map(int,sys.stdin.readline().rstrip().split(" "))
    count = 0
    for i in range(left,right+1):
        count += str(i).count("0")
    print(count)

