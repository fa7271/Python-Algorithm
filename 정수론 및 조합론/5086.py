import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0 :
        print('factor')
    elif a % b ==0 :
        print('multiple')
    else:
        print('neither')



