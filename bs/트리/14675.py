import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph =[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

question = int(input())
res = []
for _ in range(question):
    t, k = map(int,sys.stdin.readline().split(" "))
    if t == 1:
        if len(graph[k]) < 2:
            print("no")
        else:
            print("yes")
    else :
        print("yes")

