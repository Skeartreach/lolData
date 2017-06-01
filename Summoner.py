from JSONgetter import JSONgetter
from Champion import Champion
from Match import Match
class Summoner:
    def __init__(self, name):
        self.JSON = JSONgetter().getPlayerData(str(name))
        self.summonerID = self.JSON['id']
        self.accountId = self.JSON['accountId']
        self.name = self.JSON['name']
        self.profileIconId = self.JSON['profileIconId']
        self.revisionDate = self.JSON['revisionDate']
        self.champList = []

    def getRecentMatches(self):
        lastMatches = Match(self.summonerID).getById()['matches']
        return lastMatches

    def getLastChampPlayed(self):
        return Champion(Match(self.summonerID).getById()['matches'][0]['champion'])


#s = Summoner("Futit")
#print(s.getRecentMatches()['matches'][0]['timestamp'])
#print(s.getLastChampPlayed().name)