import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
RGB = []
for i in range(n):
    RGB.append(list(map(int,(input().split()))))
print(RGB)
for i in range(1,len(RGB)):

    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]
print(RGB)
print(min(RGB[-1]))
    # 26          40          83
    # 89,97   86/'83'



