import sys
sys.stdin = open('/Python/h.txt', 'r')

n = int(input())
result = n                          # 처음 결과 갯수는 처음 받은 단어갯수와 동일하게 선언
for i in range(n):
    word = input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:              #앞뒤 단어 같으면
            pass                            #패스
        elif word[j] in word[j+1:]:         # 먼저 나온 단어가 뒤에 또 나오는지 확인
            result -= 1                     # 있으면 원래 단어 갯수 -1
            break                           # 포문 탈출
print(result)
