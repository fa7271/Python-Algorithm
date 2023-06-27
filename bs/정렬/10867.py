import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N =int(sys.stdin.readline())
arr =list(map(int,sys.stdin.readline().rstrip().split(" ")))

print(*sorted(list(set(arr))))
