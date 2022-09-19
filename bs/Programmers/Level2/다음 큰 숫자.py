def solution(n):
    number = bin(n)[2:]
    print(bin(79)[2:].count('1'))
    # print(number.count('1'))
    while True:
        if bin(n+1)[2:].count('1') == number.count('1'):
            return n +1
        else:
            n += 1



print(solution(78))

