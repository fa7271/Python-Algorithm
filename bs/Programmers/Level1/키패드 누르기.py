
def solution(numbers, hand):
    answer =''

    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
           }
    left = pad['*']   #처음 왼손
    right = pad['#']  #처음 오른손
    print(pad['2'][1])
    for i in numbers:
        now = pad[str(i)] # 숫자의 키패드 위치 현재
        # 1, 4, 7을 누르는 경우
        if i in [1, 4, 7]:
            answer += 'L'
            left = now
        # 3, 6, 9를 누르는 경우
        elif i in [3, 6, 9]:
            answer += 'R'
            right = now
        # 2, 4, 6, 8 을 누르는경우
        else:
            left_dt = abs(pad[str(i)][0] - left[0] ) + abs(pad[str(i)][1] - left[1])
            right_dt =abs(pad[str(i)][0] - right[0] ) + abs(pad[str(i)][1] - right[1])
            if left_dt < right_dt :
                answer += 'L'
                left = pad[str(i)]

            elif left_dt > right_dt :
                answer += 'R'
                right = pad[str(i)]

            else :
                if hand == 'right' :
                    answer += 'R'
                    right = pad[str(i)]
                else :
                    answer += 'L'
                    left = pad[str(i)]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

# #번호와 왼손의 거리 계산
# left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
# #번호와 오른손의 거리 계산
# right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])