from collections import Counter
def solution(routes):
    routes.sort(key = lambda x:x[1])
    print(routes)
    camera = routes[0][1]
    res = 1
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            res +=1
    return res

# print(solution( 1, [2, 1, 2] ))
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
# print(solution([[-18,-15], [-17,-13], [-16,-11], [-12,-5]]))
# print(solution([[1, 15], [15,16], [16,17], [20,21]]))
