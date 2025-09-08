import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

S, P = map(int, sys.stdin.readline().rstrip().split(" "))
word = input()
keys = list(map(int, sys.stdin.readline().split(" ")))

dic = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in range(P):
    dic[word[i]] += 1
left = 0
right = P - 1
answer = 0
if dic["A"] >= keys[0] and dic["C"] >= keys[1] and dic["G"] >= keys[2] and dic["T"] >= keys[3]:
    answer += 1

for i in range(S - P):
    dic[word[left]] -= 1
    left += 1

    right += 1
    dic[word[right]] += 1
    if dic["A"] >= keys[0] and dic["C"] >= keys[1] and dic["G"] >= keys[2] and dic["T"] >= keys[3]:
        answer += 1

print(answer)
