def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        list=[]
        for j in range(len(arr1[i])):
            list.append(arr1[i][j]+arr2[i][j])

        answer.append(list)

    return answer




print(solution([[1,2],[2,3]],[[3,4],[5,6]]))