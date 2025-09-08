import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

word = list(input())
lst = []
for i in range(len(word)):
    lst.append("".join(word[i:]))
lst.sort()
print(*lst,sep ="\n")
