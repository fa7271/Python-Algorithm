def solution(data, col, row_begin, row_end):

    x = sorted(data, key =lambda x:(x[col-1],-x[0]));''
    res = []
    while row_begin<=row_end:
        ans = 0
        for i in x[row_begin-1]:
            ans += i % row_begin

        res.append(ans)
        row_begin += 1
    result = res[0]
    for i in res[1:]:
        result = result ^ i
    return result
    # print(result)



print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))