import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


(N,M) = sys.stdin.readline().split()
setword_S = set()               # 집합에 포함되어 있는 문자열들
setword = list()                # 검사할 문자열들
count = 0
for i in range(int(N)):         # 집합에 들어갈 단어들
    setword_S.add(sys.stdin.readline().rstrip())

for i in range(int(M)):         # 검사할 문자열들 리스트로 만듦
    setword.append(sys.stdin.readline().rstrip())

for i in setword:               # 검사할 문자열들 포문 쭉 돌려서
    if i in setword_S:          # 건사한 문자열이 집합에 포함돼 있으면
        count += 1              # 카운트를 1개 더해주고
print(count)                    # 출력

