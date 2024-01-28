import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())


def prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def dfs(node):
    if len(str(node)) == n:
        print(node)

    # 짝수 넣으면 어차피 2로 나누어져서 걍 홀수만 집어넣가
    for i in ([1, 3, 5, 7, 9]):
        #  다음 숫자 만들어주고
        next_node = node * 10 + i
        # 그 숫자 소수인가? 체크해줘야함
        if prime(next_node):
            # 소수이면 다음으로 넘김
            dfs(next_node)


for i in ([2, 3, 5, 7]):
    dfs(i)
