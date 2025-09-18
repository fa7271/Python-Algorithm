import sys
sys.stdin = open('/Users/song/Desktop/Python/h.txt', 'r')
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    used = set(x for x in p if x > 0)  # 이미 있는 숫자
    num = 1
    # 뒤에서부터 0 에 가장 작은 사용 안된 숫자를 채움
    for i in range(n - 1, -1, -1):
        if p[i] == 0:
            while num in used:
                num += 1
            p[i] = num
            used.add(num)
            num += 1
    print(p)

    l, r = n, -1
    for i in range(n):
        if p[i] != i + 1:
            l = min(l, i)
            r = max(r, i)
    print(l,r)
    if r == -1:   # 이미 정렬된 경우
        print(0)
    else:
        print(r - l + 1)