import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# word = list(sys.stdin.readline().rstrip())
# N = int(sys.stdin.readline())
# lis = [[0]*26 for i in range(len(word))]
# lis[0][ord(word[0]) - 97] = 1
# for i in range(1, len(word)):
#     lis[i][ord(word[i]) - 97] = 1
#     for j in range(26):
#         lis[i][j] += lis[i - 1][j]
# for i in range(N):
#     w, left, right = sys.stdin.readline().rstrip().split(" ")
#     left, right = int(left),int(right)
#     w = ord(w)-97
#
#     if left > 0:
#         print(lis[right][w] - lis[left-1][w])
#     else:
#         print(lis[right][w])



    # print(lis[left][w])

# for i in range(N):
#     w, left, right = sys.stdin.readline().rstrip().split(" ")
#     count = 0
#     for i in range(int(left),int(right)+1):
#         if word[i] == w:
#             count +=1
#     print(count)

import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1
