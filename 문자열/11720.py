import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
# input = sys.stdin.readline

n = input()

print(sum(list(map(int,input()))))