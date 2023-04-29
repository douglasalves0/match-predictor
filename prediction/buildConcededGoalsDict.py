def getConcededGoalsDict(teamList):
    answer = {}
    for team in teamList:
        answer[team['time']['sigla']] = team['gols_contra']
    return answer