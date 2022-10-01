from operator import index

def solution(msg):
    res = []
    dic = {chr(i): i-64 for i in range(ord('A'),ord('Z')+1)}
    num = 27
    while msg:
        start = 1
        while msg[:start] in dic.keys() and start <= len(msg):
            start += 1
        res.append(dic[msg[:start -1]])
        dic[msg[:start]] = num
        num += 1

        msg = msg[start-1:]
    return res


print(solution(	"TOBEORNOTTOBEORTOBEORNOT"))



