def axb(aScoredGoals, aConcededGoals, bScoredGoals, bConcededGoals, aMatches, bMatches):
    
    aAvgScoredGoals = aScoredGoals / aMatches
    bAvgScoredGoals = bScoredGoals / bMatches

    aAvgConcededGoals = aConcededGoals / aMatches
    bAvgConcededGoals = bConcededGoals / bMatches

    aExpectedGoals = (aAvgScoredGoals + bAvgConcededGoals) / 2
    bExpectedGoals = (bAvgScoredGoals + aAvgConcededGoals) / 2

    return (aExpectedGoals, bExpectedGoals)