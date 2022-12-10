# O(n^2) time | O(k) space where n is the number of competitions and k is the number of teams
def tournamentWinner(competitions, results):
    # competitions [ [homeTeam, awayTeam] ]
    # results: 0 = away team won | 1 = home team won
    # 3 points for winner and 0 points for loser

    # associate each result with the comp in the array respectively
    #create hash table to keep track of scores

    scoreboard = {}
    match = 0

    for team in competitions:
        #grab the winning team and put them in hash table with num of points as value
        if results[match] == 0:
            #if away team wins then take that value and add it to table with value += 3
            winner = competitions[match][1]
            if winner not in scoreboard:
                scoreboard[winner] = 3
            else:
                scoreboard[winner] += 3
        #home team wins
        else:
            winner = competitions[match][0]
            if winner not in scoreboard:
                scoreboard[winner] = 3
            else:
                scoreboard[winner] += 3
        #increment match by 1 for each iteration
        match += 1

    comp_winner = max(scoreboard, key=scoreboard.get)

    return comp_winner


#constant variable
HOME_TEAM_WON = 1

#O(n) time | O(k) space - where n is the number of
#competitions and k is the number of teams


def tournamentWinner(competitions, results):
    #track currentBestTeam which is team with most points
    currentBestTeam = ""
    #track scores across teams using hash table
    scores = {currentBestTeam: 0}

    for index, competition in enumerate(competitions):
        #grab the result for each mach at given index from results array
        result = results[index]

        #unpack competition array
        homeTeam, awayTeam = competition

        #set winnning team using constnat varible to check
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        #updates score hash table by passing in winningTeam, points and hashtable
        updateScores(winningTeam, 3, scores)

        #check which team has the leading score and set that as the currentBestTeam
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    #return name of winner
    return currentBestTeam


def updateScores(team, points, scores):
    #if team not in table create a new key:value
    if team not in scores:
        scores[team] = 0

    #update its value by the num of points
    scores[team] += points
