import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

left_word, right_word = input().split("*")

for _ in range(N):
    x = input()
    if len(x) < len(left_word) + len(right_word):
        print("NE")
    elif left_word == x[:len(left_word)] and right_word == x[-len(right_word):]:
        print("DA")
    else:
        print("NE")
