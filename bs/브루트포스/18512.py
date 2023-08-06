import sys

X,Y,A,B = map(int,sys.stdin.readline().split(" "))

sets_A = set()
sets_B = set()
for i in range(A,1000000,X):
    sets_A.add(i)
for i in range(B,1000000,Y):
    sets_B.add(i)
res = sets_A&sets_B
if len(res) > 0 :
    print(sorted(list(res))[0])
else:
    print(-1)

