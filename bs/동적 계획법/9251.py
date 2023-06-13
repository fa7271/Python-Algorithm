import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)

lst1 = [ i for i in sys.stdin.readline().rstrip()]
lst2 = [ i for i in sys.stdin.readline().rstrip()]

dp = [[0]*(len(lst2)+1) for _ in range(len(lst1)+1)]
for i in range(1,len(lst1)+1):
    print(i)
    for j in range(1,len(lst2)+1):
        if lst1[i-1] == lst2[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp)
print(dp[len(lst1)][len(lst2)])