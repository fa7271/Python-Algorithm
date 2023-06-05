import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

count = 1
N = int(input())
stk = []
res = []

for i in range(N):
    num = int(input())
    while count <= num:
        stk.append(count)
        res.append("+")
        count += 1
    if stk[-1] == num:
        stk.pop()
        res.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        print("NO")
        exit(0)
for i in res:
    print(i)
# if flag == False:
#     print("NO")
# else:
#     for i in res:
#         print(i)



# [1,2,5,7,8]
# [4,3,6,8,7,5,2,1]