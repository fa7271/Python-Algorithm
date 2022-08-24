import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')



def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer
