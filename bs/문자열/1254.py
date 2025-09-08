import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

word = sys.stdin.readline().rstrip()

for i in range(len(word)):

    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break

