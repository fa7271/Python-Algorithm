def solution(t, p):
    list = []
    x,y = 0,len(p)
    while len(t)-x >= y  :
        list.append(t[x:x+y])
        x += 1

    return len([i for i in list if int(i) <= int(p)])
print(solution("3141592", "271"))
# print(solution(	"500220839878", "7"))
# print(solution(	"10203", "15"))