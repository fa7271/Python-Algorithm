
def solution(array):
    dict = {x : 0 for x in array}
    if len(array) == 1:
        return array[0]
    for i in array:
        if i in dict:
            dict[i] += 1
    sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    return -1 if sorted_dict[0][1] == sorted_dict[1][1] else sorted_dict[0][0]



from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]

    # return -1 if max(dict.values() >=2) else max(dict)
# print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1,2,3,3,3,4,4]))
print(solution([5]))

# print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))



