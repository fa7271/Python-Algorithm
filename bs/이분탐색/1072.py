import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

x,y= map(int,input().split())
z = (100*y)//x
left = 0
right = x
res = 0
if z>=99 or x==y:
    print(-1)
else:
    while left<=right:
        mid=(left+right)//2 # 중간 값 만큼 이켜주고
        if (100*(y+mid))//(x+mid)>z: # 중간 그게 z보다 크면
            res=mid # 결과르 바꿔주고
            right=mid-1 # 폭을 줄여봄
        else: # 중간보다 작으면
            left=mid+1 # 좀더 넓혀봄
    print(res)