import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


s1 = input()
s2 = input()
if s1*len(s2) == s2*len(s1):
    print(1)
else:
    print(0)