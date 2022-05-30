import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline


N = int(input())
a = map(int,input().split())
list = list()
for i in a:
    list.append(i)

list.sort()
print(max(list) * min(list))
# sorted_list = sorted(list)
# print(sorted_list)



