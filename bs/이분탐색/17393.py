import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(input())

lst_A = list(map(int,sys.stdin.readline().rstrip().split(" ")))
lst_B = list(map(int,sys.stdin.readline().rstrip().split(" ")))
result = []
for i in range(0,len(lst_B)-1):
    now = lst_A[i]
    start = i+1; end = len(lst_B)-1
    res = i
    while start <= end:
        mid = (start+end) // 2

        if now < lst_B[mid]:
            end = mid -1
        else:
            start = mid +1
            res = mid
    result.append(str(res-(i+1)+1))

result.append(0)
print(*result)



