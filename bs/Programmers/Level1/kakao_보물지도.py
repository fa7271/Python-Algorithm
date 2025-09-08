def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] or arr2[i])
        print(tmp)
        tmp = tmp[2:].zfill(n)
        # 앞에 두개 짜르고 뒤에 n 자릿수 만큼만큼 0 차운다
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28] ))