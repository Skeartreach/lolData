from Summoner import Summoner
from Match import Match
from Champion import Champion

d = Summoner("Futit")
c = Champion().getById(40)
m = Match(d.name).getRecent()


print(c)
