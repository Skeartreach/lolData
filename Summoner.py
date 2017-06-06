import datetime
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

    def getLastMatch(self):
        return Match(self.summonerID).getById()['matches']

    def getLastMatchTime(self):
        timestampnontreated = str(s.getLastMatch()[0]['timestamp'])
        timestamp = ""
        for x in range(0, 10):
            timestamp += timestampnontreated[x]
        return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d-%m-%Y %H:%M:%S')


s = Summoner("Futit")

print(s.getLastChampPlayed().name)
print(s.getLastMatchTime())