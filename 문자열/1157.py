import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
# input = sys.stdin.readline

word = input().upper() #대소문자 구별
word_list = list(set(word))
cnt = []
for i in word_list:    ## word_list = [b,a,g]
    count = word.count(i)
    cnt.append(count)
    # print(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])
###############################

n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
    result.append(n.count(i))
if result.count(max(result)) > 1:
    print("?")
else:
    print(alpa[result.index(max(result))])

