def getScoredGoalsDict(teamList):
    answer = {}
    for team in teamList:
        answer[team['time']['sigla']] = team['gols_pro']
    return answer