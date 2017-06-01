from JSONgetter import JSONgetter
from Summoner import Summoner
class Match:
    def __init__(self, name):
        self.player = Summoner(name)
        self.JSON = JSONgetter().getRecentMatches(self.player.accountId)

    def getRecent(self):
        return self.JSON