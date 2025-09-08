from collections import Counter


def solution(participant, completion):

    res = Counter(participant) - Counter(completion)
    return "".join(list(res.keys()))
    # return ''.join([i for i in participant if i not in completion])

print(solution( ["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
