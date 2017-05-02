import sys
import random

#03.05.2017 - 01:56 Berkin Akaydın

class Week:
    weekNo = 1
    playList = None

    def __init__(self, weekNo):
        self.weekNo = weekNo
        self.playList = list()

    def addMatch(self, Match):
        self.playList.append(Match)

    def printWeek(self, weekNo):
        for matches in self.playList:
            print("%d %s %s" % (self.weekNo, matches.hostTeam.teamName,
                                matches.guestTeam.teamName))

    def setMatch(self, Week, teams):
        teamCount = len(teams)
        failCount = 0
        while True:
            homeSideId = random.randint(0, teamCount - 1)
            if(teams[homeSideId].isSelectedBefore is False):
                teams[homeSideId].isSelectedBefore = True
                tempHomeSideId = homeSideId
                break

        while True:
            awaySideId = random.randint(0, teamCount - 1)
            while True:
                if(awaySideId != homeSideId):
                    break
                else:
                    awaySideId = random.randint(0, teamCount - 1)
                    
            if(teams[awaySideId].isSelectedBefore is False):
                teams[awaySideId].isSelectedBefore = True
                teams[homeSideId].guestTeams.append(teams[awaySideId])
                break

        newMatch = Match(teams[homeSideId],teams[awaySideId])
        Week.addMatch(newMatch)

    def nextWeek(self, teams):
        self.weekNo = self.weekNo + 1
        for team in teams:
            team.isSelectedBefore = False

class Match:
    hostTeam = None
    guestTeam = None

    def __init__(self, hostTeam, guestTeam):
        self.hostTeam = hostTeam
        self.guestTeam = guestTeam

    def printMatch(Match):
        print("%s %s" % Match.hostTeam.teamName, Match.guestTeam.teamName)

class Team:
    teamName = ""
    teamId = 0
    awaySideCount = 0
    homeSideCount = 0
    isSelectedBefore = False
    guestTeams = None

    def __init__(self, teamName, teamId, homeSideCount, awaySideCount):
        self.teamName = teamName
        self.teamId = teamId
        self.homeSideCount = homeSideCount
        self.awaySideCount = awaySideCount
        self.guestTeams = list()

    def printTeams(self, team):
        print("%d - %s  " % (team.teamId, team.teamName))

    def setSelected(self, isSelectedBefore):
        self.isSelectedBefore = isSelectedBefore

def initTeams(teams):
    teamId = 0
    teamCount = 18
    awaySideCount = teamCount - 1
    homeSideCount = awaySideCount
    nameId = 65  # Name is created with reference to ascii table

    for i in range(0, teamCount):
        teamName = chr(nameId)
        nameId = nameId + 1
        teamId = i
        newTeam = Team(teamName, teamId, homeSideCount, awaySideCount)
        teams.append(newTeam)

    return teamCount

def main(argv):
    teams = list()
    teamCount = initTeams(teams)
    
    for i in range(0, (teamCount - 1) * 2):
        weekNo = i + 1
        matchWeek = Week(weekNo)
        
        for j in range(0, int((teamCount / 2))):
            matchWeek.setMatch(matchWeek, teams)
        matchWeek.printWeek(i)
        matchWeek.nextWeek(teams)
        print("---------NEXT WEEK---------")

if __name__ == "__main__":
    main(sys.argv)