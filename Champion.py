import time
from JSONgetter import JSONgetter
class Champion:
    def __init__(self):
        self.JSON = ""
        self.id = 1
        self.key = ""
        self.name = ""
        self.title = ""

    def getById(self,id):
        self.JSON = JSONgetter().getChampionById(id)
        self.id = self.JSON['id']
        self.key = self.JSON['key']
        self.name = self.JSON['name']
        self.title = self.JSON['title']