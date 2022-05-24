import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())



n = int(input())
arr = list(map(int, input().split()))
arr_list = sorted(list(set(arr)))       # 중복제거
arr_dic = {}

for i in range(len(arr_list)):          # arr_list 에 길이만큼 포문을 돌려
    arr_dic[arr_list[i]] = i            # 딕셔너리를 만들어준다
for i in range(n):                      # 입력받은 n 만큼 포문을 돌려
    arr[i] = arr_dic[arr[i]]            # 딕셔너리에서 키에 arr[i]를 넣어 벨류를 찾아 arr를 만들어줌
print(arr)
print(*arr)

# * 는 언팩킹 [] 까줌

# for i in range(n):
#     print(arr[i], end = ' ')


