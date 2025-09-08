import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
res = set()
temp_result = []
def bt():
    if temp_result:
        res.add(int("".join(map(str, temp_result))))
    #    감소하는 가장 큰 수 = 9876543210 => 10자리 만들면됨.
    for i in range(10):
        if not temp_result or temp_result[-1] > i:
            temp_result.append(i)
            bt()
            temp_result.pop()

bt()
res = sorted(res)
try:
    print(res[n-1])
except:
    print(-1)

