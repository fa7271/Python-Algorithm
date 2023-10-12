import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, l = map(int,input().split())
S = [int(input()) for i in range(m)] +[l]
Q = [int(input()) for i in range(n)]

def find_count(mid):
    # 잘라서 나오는 갯수, 자르고 나서 위치 저장한 변수
    cnt,temp = 0, 0
    for i in S:
        # 자른 크기가 잘라야 하는 값보다 크면
        if i - temp >= mid:
            # 자를 수 있으므로 갯수 추가
            cnt += 1
            # 그 다음 자를 위치를 위해 이동
            temp = i
    return cnt


for i in Q:
    # 제일 작은크기는1, 제일 큰 크기는 l
    left = 1; right = l; res = 0

    while left <= right:
        # 잘라야 하는 값
        mid = (left + right) // 2
        # mid 를 들고 갔을때 몇개의 조각이 나오는지 확인
        count = find_count(mid)
        #조각이 많이 나오면 잘라야 하는 크기를 늘리고
        if count > i:
            left = mid +1
            res = max(mid,res)
        # 조각이 적게 나오면 잘라야 하는 크기를 줄인다.
        else:
            right = mid-1
    print(res)