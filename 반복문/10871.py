import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')


input = sys.stdin.readline

a,b = map(int,(input().split()))    #입력받은 N,X map함수 사용해서 int로 변환
c = list(map(int,input().split()))  #입력받은 수열 A 리스트로 받음
print(c)
result = ''
for i in c:
    if i<b:                     #  리스트 c에 있는거 하나씩 빼와서  b 보다 작을때
        #print(type(i))         # i에 type은 int
        #print(type(result))    # result 에 type 은 str
        result +=str(i)+ ' '    # type 이 맞춰주기위해 str(i)를 써줌
print(result)