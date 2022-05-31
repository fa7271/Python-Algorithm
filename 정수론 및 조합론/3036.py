import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
input = sys.stdin.readline

                                                    #유클리드 호제법
def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n

    return a

n = int(input())
li = list(map(int, input().split()))
print(li)
for i in range(1, n):
    g = gcd(li[0], li[i])                           # 최대 공약수 구해옴
    print('{0}/{1}'.format(li[0]//g, li[i]//g))     # 최대공약수로 나눠주면 원하는 값 출력