import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


(N,M) = sys.stdin.readline().split()  # N은 듣잡 M은 보잡

list1 = set()
list2 = set()
for i in range(int(N)):
    list1.add(sys.stdin.readline().rstrip())

for i in range(int(N)+1):
    list2.add(sys.stdin.readline().rstrip())

result = sorted(list(list1&list2))
print(len(result))
for i in result:
    print(i)

