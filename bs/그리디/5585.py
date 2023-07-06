import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

money = 1000- int(sys.stdin.readline())
lst =[500,100,50,10,5,1]
idx = 0
cnt = 0
while money > 0:
    cnt += money // lst[idx]
    money %= lst[idx]
    idx+=1
print(cnt)
