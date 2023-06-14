import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N, M = map(int,sys.stdin.readline().split(" "))
word = dict()

for i in range(N):
    w = sys.stdin.readline().rstrip()
    if len(w) >= M:
        if w not in word:
            word[w] = 1
        else:
            word[w] += 1
# word = sorted(word, key=lambda x: (-x[1], x[0]), reverse=True)
word = sorted(word.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
for i in word:
    print(i[0])