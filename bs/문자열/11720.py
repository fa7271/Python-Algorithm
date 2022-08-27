import sys
sys.stdin = open('/Python/h.txt', 'r')
# input = sys.stdin.readline

n = input()

print(sum(list(map(int,input()))))