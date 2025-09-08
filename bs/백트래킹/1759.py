import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N, M = map(int,sys.stdin.readline().rstrip().split(" "))
lst = sorted(list(sys.stdin.readline().rstrip().split(" ")))
arr = []
word = ["a","e", "i", "o", "u"]
def bt(idx):
    # 길이가 같다면
    if len(arr) == N:
        # 제한사항 체크해줘야함
        a, b = 0, 0
        for i in arr:
            if i in word:
                a +=1
            else:
                b+=1
        if a >=1 and b >= 2:
            print("".join(arr))
            return
        return
    for i in range(idx,M):
        arr.append(lst[i])
        bt(i+1)
        arr.pop()
bt(0)




