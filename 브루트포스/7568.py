import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

n = int(input())
list = list()
for i in range(1,n+1):
    x,y = map(int,(input().split()))
    list.append((x,y))                      # 몸무게와 키 리스트에 넣어줌

# print(list)
for i in list:                              # 리스트에서 뽑음
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:     # 자기보다 크고 무거운 사람이 몇명있는지 찾으면 됨
            rank +=1                        # 있으면 늘려주기
    print(rank, end = " ")

