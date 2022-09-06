
def solution(array, commands):
    answer = []
    # print(array[0:3]) # 1,5,2
    # print(array[1:5]) # 5,2,6,3
    x =[]

    for i in range(len(commands)):
        x.append(sorted(array[commands[i][0]-1:commands[i][1]]))

    for i in range(len(commands)):
        answer.append(x[i][commands[i][2] - 1 ])
    return answer

# return [sorted(array[a-1:b])[c-1] for a,b,c in commands]


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))