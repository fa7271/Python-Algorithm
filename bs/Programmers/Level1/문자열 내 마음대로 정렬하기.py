def solution(strings, n):

    return sorted({x : x[n] for x in sorted(strings)}, key = lambda x : (x[n],x) )


    # return sorted(strings, key = lambda x : (x[n],x) )
print(solution(["sun", "bed", "car"],1))

# return strings.sort(key = lambda x : x[n])

