from urllib.request import urlopen
import re

class FilthyLoLPlayer:

    def __init__(self, summoner_name, league, division, lp, wins, loses):
        self.summoner_name = summoner_name
        self.league = league
        self.division = division
        self.lp = lp
        self.wins = int(wins)
        self.loses = int(loses)
    
    def showInfo(self):
        print(f'{self.summoner_name} -- {self.league} -- {self.division} -- {self.lp} -- {self.wins} -- {self.loses} -- {(self.wins / (self.wins + self.loses))*100}% -- ')



urls = ["https://www.op.gg/summoners/las/JackSm",
        "https://www.op.gg/summoners/las/fizz%C3%A4rrap",
        "https://www.op.gg/summoners/las/starseizer",
        "https://www.op.gg/summoners/las/Zyaenn",
        "https://www.op.gg/summoners/las/duketo%20pa",
        "https://www.op.gg/summoners/las/INR%20Manuelift",
        "https://www.op.gg/summoners/las/tomvsjr",
        "https://www.op.gg/summoners/las/ilkartty"]

players = []

def info_extracter(html):
    summoner_name = re.search("<span class=\"summoner-name\">(.*)</span>", html).group(1)
    all_info = re.search("<div class=\"tier\">(.*)</div></div></div></div><style data-emotion=\"css 1474l3c\">.css-1474l3c{margin-top:8px;border-radius:4px;background-color:#FFF;background-color:var", html)
    #print(all_info.group(1))
    ranked_info = re.search("([a-zA-Z]*)<!-- --> ([0-9]).*\"lp\">([0-9]{1,2})", 
                            all_info.group(1))
    league = ranked_info.group(1)
    division = ranked_info.group(2)
    lp = ranked_info.group(3)

    wins_lose = re.search("<div class=\"win-lose\">([0-9]{1,3})(W|V)<!-- --> <!-- -->([0-9]{1,3})L",
                         all_info.group(1))
    wins = wins_lose.group(1)
    loses = wins_lose.group(3)
    return FilthyLoLPlayer(summoner_name, league, division, lp, wins, loses)

def main():
    for url in urls:
        print(url)
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        players.append(info_extracter(html))
    for player in players:
        player.showInfo()
main()