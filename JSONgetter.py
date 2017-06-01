import requests

class JSONgetter:
    def __init__(self):
        #COSNTANT API KEY
        self.API_KEY = "RGAPI-3f63515c-1912-4d80-8291-4c18ed66c9c6"

        #CONSTANTS
        self.AUTH_URL = "?api_key="+self.API_KEY
        self.API_URL_CHAMP = ""
        self.API_URL_SUMMONER = ""
        self.SUMMONER_NAME = ""
        self.API_FULL_URL = ""

    def getPlayerData(self, playerName):
        self.SUMMONER_NAME = playerName
        self.API_URL_SUMMONER = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
        self.API_FULL_URL = self.API_URL_SUMMONER + self.SUMMONER_NAME + self.AUTH_URL
        return requests.get(self.API_FULL_URL).json()

    def getPlayerId(self, playerName):
        self.SUMMONER_NAME = playerName
        self.API_URL_SUMMONER = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
        self.API_FULL_URL = self.API_URL_SUMMONER + self.SUMMONER_NAME + self.AUTH_URL
        return requests.get(self.API_FULL_URL).json()['accountId']

    def getChampionById(self, id):
        self.API_URL_CHAMP = "https://global.api.riotgames.com/api/lol/static-data/EUW/v1.2/champion/"
        self.CHAMPION_ID = id
        self.API_FULL_URL = self.API_URL_CHAMP + str(self.CHAMPION_ID) + self.AUTH_URL
        return requests.get(self.API_FULL_URL).json()

    def getRecentMatches(self, accountID):
        self.API_URL_MATCHES = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/"
        self.API_POST_URL = "/recent"
        self.API_FULL_URL = self.API_URL_MATCHES + str(accountID) + self.API_POST_URL + self.AUTH_URL
        return requests.get(self.API_FULL_URL).json()
