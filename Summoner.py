from JSONgetter import JSONgetter
class Summoner:
    def __init__(self, name):
        self.JSON = JSONgetter().getPlayer(str(name))
        self.summonerID = self.JSON['id']
        self.accountId = self.JSON['accountId']
        self.name = self.JSON['name']
        self.profileIconId = self.JSON['profileIconId']
        self.revisionDate = self.JSON['revisionDate']

    def getRecentMatches(self):
       return JSONgetter().getRecentMatches(self.accountId)