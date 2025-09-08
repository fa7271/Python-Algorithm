import numpy as np

# def solution(arr1, arr2):
#     return np.dot(arr1,arr2).tolist()
def solution(arr1, arr2):
    print(len(arr1[0]))
    list = [len(arr2[0]) * [0] for i in range(len(arr1))]
    for i in range(len(arr1)):  # 행
        for j in range(len(arr2[0])): # 열
            for k in range(len(arr1[0])): # 행 돌면서 열이랑 곱함
                list[i][j] += arr1[i][k] * arr2[k][j]
    return list
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
