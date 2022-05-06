
import sys
sys.stdin = open('h.txt','r')
# input = sys.stdin.readline

# data = sys.stdin.read()
#
# # data2 = data%42r
# l=[int(input())for i in range(9)]
# print(max(l),l.index(max(l))+1)

# a = []
# for i in range(9):
#     a.append(int(input()))
# print(max(a))
# print(a.index(max(a))+1)


# 백준 나머지
# s = set()
# for i in range(10):
#     s.add((int(input())%42))
# print(s)
# print(len(s))


# 1546번
# n = int(input())
# a = list(map(int,input().split()))
# m = int(max(a))
# sum = 0
# for i in range(n):
#     a[i] = a[i]/m*100
#     sum += a[i]
# print(sum/n)
#
# 8958번
# n = int(input())
# for i in range(n):
#     a = input()
#     sum = 0
#     sumpoint = 0
#     for j in a:
#         if j == 'O':
#             sumpoint += 1
#         else:
#             sumpoint = 0
#         sum += sumpoint
#     print(sum)
#

# 4334번
# n = int(input())
# for i in range(n):
#     a = list(map(int,input().split(" ")))
#     avg = sum(a[1:])/a[0]
#     count = 0
#
#     for j in range(1,len(a)):
#         if a[j] > avg:
#             count += 1
#     result = count / a[0] * 100
#     print('%.3f'% result + '%')
#

# 15596번
# def solve(a):
# return sum(a)

# 4673번
# def d(n) :
#    n = n + sum(map(int,str(n)))
#    return n
# notself = set()
#
# for i in range(1,10001):
#     notself.add(d(i))
# for j in range(1,10001):
#     if j not in notself:
#         print(j)

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오

#1065
# hansu = 0
# num = int(input())
# for i in range(1, num+1):
#     if i < 100:
#         hansu += 1
#     else :
#         n = list(map(int,str(i)))
#         if n[2]-n[1] == n[1]-n[0]:
#             hansu += 1
# print(hansu)
# --------------------
# def h(n):
#     if n<100:
#         return True
#     if (n%100//10)*2==n//100+n%10:
#         return True
#     return False
# c = 0
# for i in range(int(input())):
#     if h(i+1):
#         c+=1
# print(c)

print(1)




























