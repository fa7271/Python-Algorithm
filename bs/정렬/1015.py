import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(map(int,input().split()))
sorted_list = sorted(lst)
res = []
for i in range(n):
    idx = sorted_list.index(lst[i])
    res.append(idx)
    print(lst[i],idx, sorted_list,"res : ", res)
    sorted_list[idx] = False
print(res)