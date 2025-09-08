

def solution(storey):
    arr =[int(i) for i in str(storey)]
    count = 0
    while len(arr) > 0:
        number = arr.pop()
        if number > 5:
            if len(arr) == 0:
                print(number,arr,count)
                count += (10 - number) + 1
                break
            else:
                count += 10 - number
                next_number = arr.pop()
                next_number += 1
                arr.append(next_number)
        elif number == 5:
            if len(arr) == 0:
                count += 5
                break
            next_number = arr.pop()
            if next_number < 5:
                count += number
                arr.append(next_number)
            else:
                count += number
                arr.append(next_number+1)
        else:
            count += number
    return count
# print(solution(66))
# print(solution(6))
print(solution(2554))
# print(solution(45))
# print(solution(75)) #100 - 20 - 50 / 70 + 50 / 80 - 5
# print(solution(555))
# print(solution(155))
