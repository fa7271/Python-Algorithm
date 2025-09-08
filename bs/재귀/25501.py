import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())


def recursion(s, l, r):
    if l >= r: return 1,l
    elif s[l] != s[r]: return 0,l
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
for i in range(n):

    isp, recu =isPalindrome(input().strip("\n"))
    print(isp, recu+1) # 0부터 했으니
