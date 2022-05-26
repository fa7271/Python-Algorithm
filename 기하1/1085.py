import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())




(x,y,w,h) = map(int,input().split())
print(min(x,y,h-y,w-x))
