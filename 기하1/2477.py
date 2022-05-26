import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
# input = sys.stdin.readline
# input = int(sys.stdin.readline())


k = int(input())
a_li = []

w = h = w2 = h2 = 0

for i in range(6):
    x,a = map(int, input().split())
    a_li.append(a)
    if i % 2 == 0:              # 나머지
        w = max(w, a)
    else:
        h = max(h, a)
# 최댓값을 정해줌
# 가로 세로 순으로 바뀌므로 나머지 % = 0 이용

# 두번씩 나온애들 사이에 껴있는애들이 작은 사각형 높이와 너비임
# 작은 사각형

for i in range(6):              # 두번씩 나온 애 껴있는 애 찾는 방법 두개에 합이 높이면 w 길이나옴
    if i % 2 == 0 and h == a_li[(i+5) % 6] + a_li[(i+1) % 6]:
        w2 = a_li[i]
    elif i % 2 == 1 and w == a_li[(i+5) % 6] + a_li[(i+1) % 6]:
        h2 = a_li[i]
print(k*(w*h - w2*h2))


# for i in range(len(a_li)):
#     if a_li.count([i]):










