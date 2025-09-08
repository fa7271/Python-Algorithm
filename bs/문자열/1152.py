import sys
sys.stdin = open('../../h.txt', 'r')


n = input().split()
print(n)
print(len(n))


# # 최댓값
# word = input()
# word_list = list(set(word.replace(" ","")))
# print(word_list)
# cnt = []
# for i in word_list:
#     count = word.count(i)
#     cnt.append(count)
# print(cnt.count(max(cnt)))
