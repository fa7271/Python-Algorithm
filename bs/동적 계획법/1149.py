import sys,time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
RGB = []
for i in range(n):
    RGB.append(list(map(int,(input().split()))))
for i in range(1,len(RGB)):

    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]

start_time = time.time() # 측정 시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
print(min(RGB[-1]))
    # 26          40          83
    # 89,97   86/'83'



