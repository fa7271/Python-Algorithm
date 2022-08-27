import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N = int(sys.stdin.readline())
array = []
for i in range(N):
    array.append(list(sys.stdin.readline().split()))


array.sort(key = lambda x:int(x[0]))
for i in array:
    print(i[0],i[1])


