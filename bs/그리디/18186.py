import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, b, c = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split())) + [0, 0]
rst = 0


def number1(i):
    global rst
    rst += b * arr[i]


def number2(i):
    global rst

    buy = min(arr[i], arr[i + 1])
    rst += (b + c) * buy
    arr[i] -= buy
    arr[i + 1] -= buy


def number3(i):
    global rst
    buy = min(arr[i], arr[i + 1], arr[i + 2])
    rst += (b + (2 * c)) * buy
    arr[i] -= buy
    arr[i + 1] -= buy
    arr[i + 2] -= buy


if b <= c:
    rst = b * sum(arr)
else:
    for i in range(len(arr) - 2):

        if arr[i + 1] > arr[i + 2]:
            buy = min(arr[i], arr[i + 1] - arr[i + 2])

            rst += (b + c) * buy
            arr[i] -= buy
            arr[i + 1] -= buy

            number3(i)
            number1(i)
        else:

            number3(i)
            number2(i)
            number1(i)

print(rst)
