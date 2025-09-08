import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)


lis = []
while True:
    try:
        lis.append(int(sys.stdin.readline()))
    except:
        break

def dfs(start, end):
    if start > end :
        return
    mid = end + 1
    for i in range(start+1,end+1):
        if lis[start] < lis[i]:
            mid = i
            break
    dfs(start+1,mid-1)
    dfs(mid,end)
    print(lis[start])


dfs(0,len(lis)-1)