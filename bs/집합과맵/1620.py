import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


(N,M) = sys.stdin.readline().split() # 도감에 있는 포켓몬 갯수 N 문제갯수

dict = {}
# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고,
# 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해.
for i in range(1,int(N)+1):
    word = sys.stdin.readline().rstrip()
    dict[i] = word
    dict[word] = i                  # dict 을 만들어줌 몬스터가 키일때 숫자가 키일때 둘다

for i in range(int(M)):
    check_word = sys.stdin.readline().rstrip()
    if check_word.isdigit():               # 숫자인지 확인하는 메소드
        print(dict[int(check_word)])       # 숫자면 영어 출력하고
    else:
        print(dict[check_word])



