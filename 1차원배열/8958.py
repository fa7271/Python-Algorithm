
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

n = int(input())            # 테스트케이스 입력
for i in range(n):
    a = input()             #한줄 받아옴
    sum = 0                 #합 0 으로 선언
    sumpoint = 0            #연속된 합 0 으로 선언
    for j in a:
        if j == 'O':        # o 가 연속되면 1씩 더해줌
            sumpoint += 1
        else:               # x 가 나오면 0 으로 만듦
            sumpoint = 0
        sum += sumpoint
    print(sum)



# n = int(input())
# for i in range(n):
#     ans = sys.stdin.readline().rstrip()
#     res = 0
#     print(ans.split('X'))   #['OO', '', 'O', '', 'OOO']
#     for j in ans.split('X'):
#         k = j.count('O')
#         res += k*(k+1)/2
#
#     print(int(res))


