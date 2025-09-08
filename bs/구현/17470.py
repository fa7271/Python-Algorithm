import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, r = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
orders = list(map(int, sys.stdin.readline().rstrip().split()))
List = [[0, 1], [3, 2]]
# 상하반전여부, 좌우반전여부, 회전방향여부
result = [False, False, 0]

def number_1():
    # 좌우 먼저 하고 돌리면 됨
    if result[2] % 2:
        result[1] = not result[1]
    else:
        result[0] = not result[0]

    global List
    # 뒤집어
    List[0], List[1] = List[1], List[0]


def number_2():
    # 위에랑 반대로 가면됨
    if result[2] % 2:
        result[0] = not result[0]
    else:
        result[1] = not result[1]

    global List

    List[0][1], List[0][0] = List[0][0], List[0][1]
    List[1][1], List[1][0] = List[1][0], List[1][1]


# 왼쪽
def number_3():
    # 회전 체크
    result[2] = (result[2] + 1) % 4
    # 돌려
    number_5()


# 왼쪽
def number_4():
    # 회전 체크
    result[2] = (result[2] - 1) % 4
    # 돌려
    number_6()


def number_5():
    global List


    new_sample = [[0, 0], [0, 0]]

    new_sample[0][0] = List[1][0]
    new_sample[0][1] = List[0][0]
    new_sample[1][0] = List[1][1]
    new_sample[1][1] = List[0][1]

    List = new_sample.copy()


def number_6():
    global List
    new_sample = [[0, 0], [0,  0]]

    new_sample[0][0] = List[0][1]
    new_sample[0][1] = List[1][1]
    new_sample[1][0] = List[0][0]
    new_sample[1][1] = List[1][0]

    List = new_sample.copy()


# 우회전
def rotate(pattern):
    return list(list(zip(*pattern[::-1])))


for order in orders:
    if order == 1:
        number_1()
    elif order == 2:
        number_2()
    elif order == 3:
        number_3()
    elif order == 4:
        number_4()
    elif order == 5:
        number_5()
    elif order == 6:
        number_6()
N = n // 2
M = m // 2
section = [[row[:M] for row in graph[:N]], [row[M:] for row in graph[:N]], [row[M:] for row in graph[N:]],
           [row[:M] for row in graph[N:]]]
# 상하반전
if result[0]:
    section[0].reverse()
    section[1].reverse()
    section[2].reverse()
    section[3].reverse()
# 좌우반전
if result[1]:
    section[0] = [row[::-1] for row in section[0]]
    section[1] = [row[::-1] for row in section[1]]
    section[2] = [row[::-1] for row in section[2]]
    section[3] = [row[::-1] for row in section[3]]

for _ in range(result[2]):
    section[0] = rotate(section[0])
    section[1] = rotate(section[1])
    section[2] = rotate(section[2])
    section[3] = rotate(section[3])
# 구간 1과 구간 2의 결과를 이어 붙이기
top_result = []
for row in range(len(section[List[0][0]])):
    # 각 행을 이어붙여서 새로운 리스트에 저장
    top_result.append(section[List[0][0]][row] + section[List[0][1]][row])
# 구간 3과 구간 4의 결과를 이어 붙이기
bottom_result = []
for row in range(len(section[List[1][0]])):
    # 각 행을 이어붙여서 새로운 리스트에 저장
    bottom_result.append(section[List[1][0]][row] + section[List[1][1]][row])
total_result = top_result + bottom_result

for i in total_result:
    print(*i)
