import sys
from math import gcd

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n,m = map(int,sys.stdin.readline().rstrip().split(" "))
print(gcd(n,m))
print(m - gcd(n,m))

# 소세지 2개, 나눠 가져야 하는 사람 6 명 >> 개인당 1 / 3 씩 가져야함,
# 6 과 2의 최대공약수는 2

# 소세지 3개 사람 4명 >> 개인당 3 / 4 = 3번
# 4 10 = 2 개인당 4 / 10 > 10 - 2 = 8
# 6 8 =  2, 개인당 3/4
# 18 8 = 2 개인당 2 + 2 / 8