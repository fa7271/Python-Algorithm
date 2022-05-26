import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())

#
# (N,M) = sys.stdin.readline().split()
# A = set()
# B = set()
# for i in sys.stdin.readline().rstrip():
#     A.add(i)
#     A.discard(' ')
# for i in sys.stdin.readline().rstrip():
#     B.add(i)
#     B.discard(' ')
#
# print(len(A-B)+len(B-A))

n,m = map(int,sys.stdin.readline().split())
a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))

print(len(a-b)+len(b-a))

