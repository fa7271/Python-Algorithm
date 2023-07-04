import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,sys.stdin.readline().split(" "))
ra = N-K
num = list(sys.stdin.readline())
stack = []


for i in range(N):
    print(stack,K)
    while K > 0 and len(stack) !=0 and stack[-1] < num[i]:
        stack.pop()
        K -= 1
    stack.append(num[i])
print(stack,"So")
print(''.join(stack[:ra]))


# temp =""
# while len(temp) < N-K:
#     now = num.popleft()
#     if all(now >= i for i in num):
#         temp += str(now)
#     else:
#         num.append(now)
# print(temp)
