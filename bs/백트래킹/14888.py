import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
number = list(map(int,input().split()))
op = list(map(int,input().split()))

res = number[0]

max_value = ""
min_value = ""

def dfs(num):
    global max_value, min_value, res
    if sum(op) == 0:
        if min_value =="":
            min_value = res
        elif min_value > res:
            min_value = res

        if max_value =="":
            max_value = res
        elif max_value < res:
            max_value = res
        return

    for i in range(4):
        if op[i] > 0:
            now = res
            if i == 0:
                now += number[num]
            elif i == 1:
                res -= number[num]
            elif i == 2:
                res *= number[num]
            else:
                res = int(res/number[num])

            op[i] -= 1
            dfs(num + 1)
            res = now
            op[i] += 1

dfs(1)
print(min_value,max_value)





