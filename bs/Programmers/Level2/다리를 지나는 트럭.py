def solution(bridge_length, weight, truck_weights):

    res = 0
    bridge = [0 for i in range(bridge_length)]

    while bridge:

        res += 1 # 일단 초 추가
        bridge.pop(0) # 0을 빼므로써 한칸 전진할수있음
        if truck_weights: # 대기열에 있는한
            if sum(bridge) + truck_weights[0] <= weight: # 다리에 있는 거 + 대기열 맨앞 <= 다리 무게
                bridge.append(truck_weights.pop(0)) # # 대기열 맨앞 빼서 넣어주고
            else:
                bridge.append(0) # 아니면 뒤에 0 추가해서 한간 전진
    return res
print(solution(2, 10, [7, 4, 5, 6]))

