import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n,k = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().rstrip().split(" ")))
left, right = 0,k-1
res = []
while right < n:
    res.append(sum([i for i in lst[left:right+1]]))
    left +=1; right += 1
print(max(res))