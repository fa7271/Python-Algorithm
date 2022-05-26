import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())
# n,m = map(int,sys.stdin.readline().split())
# a = set(map(int,sys.stdin.readline().split()))
# b = set(map(int,sys.stdin.readline().split()))

# print(len(a-b)+len(b-a))

word = input()
new_word = list()

for i in range(len(word)):              # 단어의 길이만큼 반복 즉 5번
    for j in range(len(word)- i):       # 단어 끝까지만 반복해야하므로 앞에 한거 빼줌
        new_word.append(word[i:j+i+1])  # 리스트에 추가하기

print(len(set(new_word)))

