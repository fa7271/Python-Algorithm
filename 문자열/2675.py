import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
# input = sys.stdin.readline

n = int(input())
for i in range(n):
    count,word = input().split()
    for a in word:
        print(a*int(count), end='')
    print()
