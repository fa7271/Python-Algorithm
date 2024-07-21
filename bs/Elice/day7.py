import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
pow_10 = [10**i for i in range(19)]
n, k = map(int, input().split())

def cnt(x, t):
    digits = set()
    x //= pow_10[t]
    while x:
        digits.add(x % 10)
        x //= 10
    return len(digits)

def ans(x, t):
    xx = x - x % pow_10[t]
    arr = set()
    arr2 = set(range(10))
    brr = []
    brr2 = []

    x //= pow_10[t]
    while x:
        arr.add(x % 10)
        arr2.discard(x % 10)
        x //= 10

    brr2 = list(arr2)
    cn = k - len(arr)
    for j in range(cn):
        xx += pow_10[j] * brr2[cn - j - 1]
        arr.add(brr2[cn - j - 1])

    brr = list(arr)
    for j in range(cn, t):
        xx += pow_10[j] * brr[0]

    print(xx)

if cnt(n, 0) == k:
    print(n)
else:
    for i in range(0, 19):
        now = (n // pow_10[i]) % 10
        now2 = n % pow_10[i]
        for j in range(now + 1, 10):
            n -= now * pow_10[i]
            n += j * pow_10[i]
            cn = cnt(n, i)
            if cn <= k and cn + i >= k:
                ans(n, i)
                exit()
            n += now * pow_10[i]
            n -= j * pow_10[i]


