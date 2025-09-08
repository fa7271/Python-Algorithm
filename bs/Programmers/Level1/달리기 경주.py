from collections import deque


def solution(players, callings):
    # players_dict = {player:rank for rank, player in enumerate(players, start = 1)}

    rank_dic = {}
    players_dict = {}

    for idx, player in enumerate(players):
        rank_dic[idx + 1] = player
        players_dict[player] = idx + 1

    for calling in callings:
        now_rank = players_dict[calling]
        prev_rank = now_rank - 1
        prev_player = rank_dic[prev_rank]

        rank_dic[prev_rank], rank_dic[now_rank] = rank_dic[now_rank], rank_dic[prev_rank]
        players_dict[prev_player], players_dict[calling] = players_dict[calling], players_dict[prev_player]

    print(list(rank_dic.values()))

        # rankDic[cur_rank - 1], rankDic[cur_rank] = rankDic[cur_rank], rankDic[cur_rank - 1]
        # playerDic[prev_player], playerDic[cur_player] = playerDic[cur_player], playerDic[prev_player]



    # print(players_dict)
    # for i in callings:
    #     change_rank = players_dict[i] - 1 # kai 이면 3을 저장 .
    #     reverse_dict = dict(map(reversed,players_dict.items()))
    #     change_player = reverse_dict[change_rank]
    #     players_dict[change_player] += 1
    #     players_dict[i] = change_rank
    # sorted_players = sorted(players_dict, key=players_dict.get)
    # result = [player for player in sorted_players]
    # return result

    # player_calling = {i: callings.count(i) for i in callings}
    # lis = [0 for i in range(len(players))]
    # for key, value in player_calling.items():
    #     players_dict[key] -= value
    #     lis[players_dict[key]-1] = key
    #     players_dict[key] = 0
    # for key,value in players_dict.items():
    #     if value != 0:
    #         for idx, i in enumerate(lis):
    #             if i == 0:
    #                 lis[idx] = key
    #                 break
    # print(lis)

print(solution(	["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
# 	["mumu", "kai", "mine", "soe", "poe"]