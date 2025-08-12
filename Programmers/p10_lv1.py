def solution(players, callings):
    
    player_dict = dict(zip(players, range(len(players))))
    
    for call in callings:
        pos = player_dict[call]
        player_dict[call] = pos - 1
        player_dict[players[pos - 1]] = pos
        players[pos], players[pos - 1] = players[pos - 1], players[pos]
    
    return players