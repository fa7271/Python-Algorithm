import sys
sys.stdin = open('/Python/h.txt', 'r')

def stars(n):
    array = []
    for i in range(3*len(n)):
        if i//len(n) ==1:                       # 몫이 1일때 가운데 3*3 부분
            array.append(n[i%len(n)] + " " * len(n) + n[i%len(n)]) # i 2일때
            # array.append(n[2]+ " "*3 + n[2])
        else:                                   # 나머지가 1일때
            array.append(n[i%len(n)] * 3 )
    return(list(array))

star = ["***","* *","***"]
n = int(input())

k = 0
while n != 3:
    n = int(n/3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)


# def get_stars(n):
#     matrix = [] #별을 담을 리스트 선언
#     for i in range(len(n) * 3): #인자로 전달된 리스트의 길이 * 3만큼 반복(별의 총 줄 개수가 3배씩 늘어나기 때문 ex)3 -> 9 -> 27 ...)
#         if i // len(n) == 1: #인자로 전달된 리스트의 길이로 나눈 몫이 1일 경우(즉,별모양에서 중간에 빈칸이 들어가는 경우의 범위)
#             matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)]) #해당 빈칸의 개수만큼(인자로전달된 리스트의 길이가 빈칸의 개수)별 중간에 추가해준다.
#         else:#그 외 경우
#             matrix.append(n[i % len(n)] * 3) #리스트에 저장되어있는 별의 개수 * 3배 만큼 추가해준다.(각 줄마다 별의 개수가 3배만큼 증가하기 때문)
#     return matrix #별이 저장되어 있는 리스트를 반환
#
#
# resultStar = ["***", "* *", "***"] # n==3일 때의 별 초기화
#
# n = int(input())
# count = 0 #별의 개수를 구하는 함수(get_stars) 반복횟수 구하기
#
# while n != 3: #n이 3이아닐때 반복(3이면 그냥 바로 출력)
#     n //= 3 #n을 3으로 나눈 몫을 대입
#     count += 1 #한번 나눌때 마다 count값 1씩 증가
#
# for _ in range(count): #count값 만큼 반복(n이 9이상일 때)
#     resultStar = get_stars(resultStar) #반복할 때마다 별의 개수가 줄마다 3배씩 늘어나기 때문에 늘어난 별의 개수를 그 전 개수 별의 리스트에 대입해준다.
#
# for j in resultStar: #리스트에 저장되어있는 별을 줄마다 출력
#     print(j)
