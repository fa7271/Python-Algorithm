import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
word = input()
a=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
result = 0   # 합 0선언
for i in range(len(word)):              # 입력받은 단어의 길이만큼 for문
    for j in a:                         # a리스트 안에서 포문 한번더
        if word[i] in j:                # a리스트 안에 해당하는 문자를 찾으면
            result += a.index(j) + 3    # 그 해당하는 문자열 인덱스 + 3
print(result)

