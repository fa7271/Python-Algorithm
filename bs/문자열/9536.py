import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
T = int(sys.stdin.readline())

for _ in range(T):
    word = list(map(str, sys.stdin.readline().rstrip().split(" ")))
    lst = []

    while True:
        x = list(map(str, sys.stdin.readline().rstrip().split(" ")))
        if " ".join(x) == "what does the fox say?":
            break
        lst.append(x[-1])
    res = []
    for i in word:
        if i not in lst:
            res.append(i)
    print(" ".join(res))