def solution(bandage, health, attacks):

    last_attack_time = attacks[-1][0]
    current_health = health
    dp = [0] * (attacks[-1][0]+1)

    count = 0 # 연속성공횟수 bandage[0] 만큼 해야함
    time = 0
    for x, y in attacks:
        dp[x] = y
    # 1초씩 증가
    while current_health > 0 and time < last_attack_time + 1:
        # 공격 받았으면
        if dp[time] != 0:
            # 현재체력 깎고
            current_health -= dp[time]
            count = 0
        # 공격을 안 받았으면
        else:
            current_health += bandage[1] # 체력회복
            count += 1 # 연속 성공 증가

            if count == bandage[0]: # 스킬 시간 만큼 걸렸으면
                current_health += bandage[2] # 보너스
                count = 0 # 연속 초기화
            if current_health >health:
                current_health = health
        time += 1
        if current_health < 0:
            return -1

    return current_health




print(solution([5, 1, 5],30	,[[2, 10], [9, 15], [10, 5], [11, 5]]))

