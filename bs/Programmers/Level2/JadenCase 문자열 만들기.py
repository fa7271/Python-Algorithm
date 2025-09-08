
def solution(s):
    word = ' '.join(s.split(" ")).split()
    for i in range(len(word)):
        if not word[i][0].isdecimal():
            word[i] = word[i][0].upper() + word[i][1:].lower()
    return ' ' .join(word)

def solution(s):
    arr = s.split(" ")
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return ' '.join(arr)

print(solution("333    the last week"))
