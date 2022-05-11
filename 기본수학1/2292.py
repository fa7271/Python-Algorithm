import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')



n = int(input())

line = 1
next_num = 1

if n == 1:
    print(1)
else:
    while True:
        if n <= next_num:
            print(line)
            break
        next_num += (6 * line)
        line += 1