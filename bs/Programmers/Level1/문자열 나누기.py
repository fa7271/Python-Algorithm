from collections import deque
def solution(s):
    x = deque([i for i in (s)])
    main, count = ["", 0, 0,], 0
    while x:
        i = x.popleft()
        if main[0] =="":
            main[0] += i
            main[1] +=1
        else:
            if main[0] == i:
                main[1] += 1
            else :
                main[0] == i
                main[2] +=1

            if main[1] ==main[2]:
                count += 1
                main = ["", 0, 0]
    if main != ["", 0, 0] : count+=1
    return count