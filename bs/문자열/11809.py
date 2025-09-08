import sys
sys.stdin = open('/Python/h.txt', 'r')
# input = sys.stdin.readline
#
word = input()
all = 'abcdefghijklmnopqrstuvwxyz'

for i in all:
    print(i)
    if i in word:
        print(word.index(i), end= ' ')

    else:
        print(-1, end = ' ')

# all = 'abcdefghijklmnopqrstuvwxyz'

# for i in all:
#     if i in word:
#         print(word.index(i), end = ' ')
#     else:
#         print(-1, end = ' ')

        # all = 'abcdefghijklmnopqrstuvwxyz'

# - sep=" "
# 이 옵션을 이용하게 되면 print문의 출력문들 사이에 해당하는 내용을 넣을 수 있습니다.
# 기본 값으로는 공백이 들어가 있으며 이를 사용해 원하는 문자를 입력할 수 있습니다.
# - end=" "
# 이 옵션의 경우 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있습니다.
# 기본 값으로는 개행(\n)이 들어가 있으며 이를 사용해 개행을 없애거나 원하는 문자를 입력할 수 있습니다.


##11809
# S = input()
# check = [-1]*26
#
# for i in range(len(S)):
#     if check[ord(S[i])-97] != -1:
#         continue
#     else:
#         check[ord(S[i])-97] = i
#
# for i in range(26):
#     print(check[i], end=' ')

##11809
#     n = input()
# alphabet = list(range(97,123)
#
#                 for x in alphabet:
# print(n.find(chr(x)),end=" ")