import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

numbers = str(input())

lst = []
idx = 0

if len(numbers) < 10:
    n = len(numbers)
else:
    n = 9 + (len(numbers) - 9) // 2

def bt(num):
    if num == len(numbers):
        print(*lst)
        exit()

    if numbers[num] != "0":
        one = numbers[num]
        two = numbers[num:num+2]

        if int(one) <= n and one not in lst:
            lst.append(one)
            bt(num+1)
            lst.pop()
        if int(two) <= n and two not in lst:
            lst.append(two)
            bt(num+2)
            lst.pop()
bt(0)
