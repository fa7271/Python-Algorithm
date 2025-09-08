import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

for i in range(int(input())):
    print(sorted(list(map(int,input().split(" "))),reverse=True)[2])

