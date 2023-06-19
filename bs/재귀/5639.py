import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
print(pre)
def dfs(start,end):
    if start > end:
        return
    mid = end + 1 ## 맨 오른쪽 가는게 없을 수 도 있음
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            mid = i
            # print(start,pre[start],"ahah",i,pre[i], mid)
            break
    dfs(start+1,mid-1)
    dfs(mid,end)
    print(pre[start])

dfs(0, len(pre)-1)
