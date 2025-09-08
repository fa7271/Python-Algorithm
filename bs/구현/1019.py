import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())

lst = [0 for _ in range(10)]

W = 1
for i in range(len(str(n))):
    # 9로 만들고
    X = int(str(n//10) + "9")
    # 그 차이
    rest = X - n
    # 일단 냅다 자릿수 다 넣음
    for j in range(10):
        lst[j] += (n//10+1) * W
    for k in range(10-rest, 10):
        lst[k] -= W
    # 자릿수 빼주기
    # 549 - 543 = 일때
    # 543 ~ 549 까지의 십의자리, 백의 자리 안나옴 그거 빼줌
    for number in list(str(n)[:-1]):
        number = int(number)
        lst[number] -= rest * W
    lst[0] -= W
    W *= 10
    n //= 10

print(*lst)
# https://nerogarret.tistory.com/m/36