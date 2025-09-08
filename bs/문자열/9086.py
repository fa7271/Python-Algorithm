import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


for i in range(int(input())):
    x = input()
    print(x[0]+x[-1])