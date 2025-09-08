from collections import Counter


def solution(str1, str2):

    result1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i : i+2].isalpha()]
    result2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i : i+2].isalpha()]

    if len(result1) == 0 and len(result2) == 0 : return 65536

    A = Counter(result1)
    B = Counter(result2)

    sum_AB = sum((A | B).values())
    mid_AB = sum((A & B).values())

    return int(mid_AB / sum_AB * 65536)

print(solution(	"1, 1, 2, 2, 3", "1,2,2,4,5}"))



