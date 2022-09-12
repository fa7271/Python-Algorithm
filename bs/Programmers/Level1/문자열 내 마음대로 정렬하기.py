def solution(strings, n):

    sort_string = sorted(strings)
    tuple = {x : x[n] for x in sort_string}
    return sorted(tuple, key = lambda x : (x[n],x) )


    # return sorted(strings, key = lambda x : (x[n],x) )
print(solution(["sun", "bed", "car"],1))

# return strings.sort(key = lambda x : x[n])

