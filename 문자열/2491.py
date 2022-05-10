import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

input = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   # 바뀌어야 할 크로아티아어 선어
for i in word:                                             # word 포문 돌림
    input = input.replace(i,"x")                           # word에 있는게 input에 있으면 x로 바꿈
print(len(input))
