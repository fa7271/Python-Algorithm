import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(sys.stdin.readline().rstrip())


set = set(array)                #중복값을 제거
array = list(set)
array.sort()                    # 일단 사전순으로 정렬 해주고
array.sort(key=len)             # 사전순으로 정렬된 array 를 길이순으로 정렬한다

for i in array:
    print(i)


# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로