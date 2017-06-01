from JSONgetter import JSONgetter
class Match:
    def __init__(self, id):
        self.player = id
        self.JSON = JSONgetter().getRecentMatches(id)

    def getRecent(self):
        return

    def getById(self):
        return self.JSON