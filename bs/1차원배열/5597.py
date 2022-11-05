import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

number = [i for i in range(1,31)]
for i in range(28):
    number.remove(int(input()))

for i in number:
    print(i)