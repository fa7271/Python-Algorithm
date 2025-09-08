import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())

maps = sys.stdin.readline()
print(maps.count("EW"))