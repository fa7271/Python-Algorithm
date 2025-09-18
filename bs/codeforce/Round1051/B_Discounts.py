import sys
sys.stdin = open('/Users/song/Desktop/Python/h.txt', 'r')

t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int,sys.stdin.readline().split()))
    del_count = 1
    if n <= 2:
        print("YES")
    else:
        for _ in range(len(arr)):
            temp = []
            fl = True
            for j in range(len(arr)):
                if arr[j] == n :
                    temp.append(j)

            # temp 의 원소 각 차이가 1이여야함
            for k in range(len(temp)-1):
                if temp[k] + 1 != temp[k+1]:
                    fl = False
            if not fl:
                break
            for idx in temp:
                arr[idx] -= 1
            temp.clear()
            del_count += 1
            n -= 1
        print("YES" if fl else "NO")



