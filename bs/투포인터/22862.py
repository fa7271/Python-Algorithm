import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n, m = map(int, sys.stdin.readline().split(" "))
lst = list(map(int, sys.stdin.readline().split(" ")))

end =  0
count = 0
result = 0
tmp = 0
for start in range(n):
    while count <= m and end < n:
        if lst[end] % 2 == 1:  # 홀수 이면
            count += 1
        else:
            tmp += 1
        end += 1
        if start == 0 and end == n:
            result = tmp
            break
    if count == m + 1:
        result = max(tmp, result)
    if lst[start] % 2 == 1:
        count -= 1
    else:
        tmp -= 1
print(result)

# if count == m + 1:
#     result = max(result, res)
#     if left % 2 != 0:
#         count -= 1
#     if end % 2 != 0:
#         count += 1
#     left += 1
#     end += 1
# elif lst[end] % 2 == 0:
#     res += 1
#     end += 1
# else:
#     count += 1
#     end += 1
# for i in range(n):
#     end = i; i_length = 0
#     # if lst[i] % 2==0: # 시작지점 홀짝 체크
#     #     length += 1
#     while count <= m:
#         # print(i, end,count,i_length)
#         if end > n-1:
#             break
#         if lst[end] % 2 == 0:
#             i_length += 1
#         else:
#             count +=1
#         end += 1
#     res = max(res, i_length)
#     count = 0
# print(res)
