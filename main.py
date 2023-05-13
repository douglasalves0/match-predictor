import os
import requests
from dotenv import load_dotenv
from utils.consts import leagueTableUrl
from prediction.buildScoredGoalsDict import getScoredGoalsDict
from prediction.buildConcededGoalsDict import getConcededGoalsDict
from prediction.nofmatches import nofmatches
from prediction.calculation import axb

load_dotenv()

print("Carregando...")

answer = requests.get(
    leagueTableUrl + os.environ.get("TABLE_ID") + "/tabela", 
    headers = {"Authorization": "Bearer " + os.environ.get("TOKEN")}
).json()

teamScoredGoals = getScoredGoalsDict(answer)
teamConcededGoals = getConcededGoalsDict(answer)
nofMatches = nofmatches(answer)

print("Siglas dos times:")
print(list(nofMatches.keys()))

teamA = input("Sigla do primeiro time: ")
teamB = input("Sigla do segundo time: ")

aGoals, bGoals, aScored, bScored, aConceded, bConceded = axb(
    teamScoredGoals[teamA],
    teamConcededGoals[teamA],
    teamScoredGoals[teamB],
    teamConcededGoals[teamB],
    nofMatches[teamA],
    nofMatches[teamB]
)

print()

print(f"{teamA}: {aScored:.2f} gols/jogo")
print(f"{teamA}: {aConceded:.2f} sofridos/jogo\n")

print(f"{teamB}: {bScored:.2f} gols/jogo")
print(f"{teamB}: {bConceded:.2f} sofridos/jogo\n")

print(f"Placar previsto: {teamA} {aGoals:.2f} x {bGoals:.2f} {teamB}")