import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    res = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    res.sort()
    res.pop()
    if sum(res) == n:
        print(n, " = ", " + ".join(str(i) for i in res), sep="")
    else:
        print(n, "is NOT perfect.")