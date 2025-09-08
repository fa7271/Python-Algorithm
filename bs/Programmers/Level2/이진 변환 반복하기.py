def solution(s):
    count = 0
    delete_zero = 0
    res =[]
    while True:
        if s == '1':
            break

        count += 1
        delete_zero += s.count("0")

        s = s.replace("0","")
        s = bin(len(s))[2:]
    # return [count, delete_zero]
print(solution("110010101001"))