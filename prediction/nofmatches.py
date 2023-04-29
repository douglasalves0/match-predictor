def nofmatches(teamList):
    answer = {}
    for team in teamList:
        answer[team['time']['sigla']] = team['jogos']
    return answer