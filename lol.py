import re
from urllib.request import urlopen


class FilthyLoLPlayer:
    elo = 0    #class attribute
    def __init__(self, summoner_name, league, division, lp, wins, loses):
        self.summoner_name = summoner_name
        self.league = league
        self.division = division
        self.lp = int(lp)
        self.wins = int(wins)
        self.loses = int(loses)
        self.winrate = (self.wins / (self.wins + self.loses))*100

    def set_elo(self, new_elo):
        self.elo = new_elo
        pass
    def show_info(self):
        print(f'                      {self.league.upper()} {self.division} {self.lp} PUNTOS\n            {self.wins} VICTORIAS -- {self.loses} DERROTAS -- {round(self.winrate)}% WINRATE') #-- {self.elo}
        return ""

rank_stats = {'league': {'iron':10,  'bronze':20,  'silver':30,  'gold':40,  'platinum':50,  'diamond':60,  'master':70,  'grandmaster':80,  'challenger': 90},
 'division': {'1': 20, '2': 15, '3': 10, '4': 5}
 }

urls = ["https://www.op.gg/summoners/las/JackSm",
        "https://www.op.gg/summoners/las/fizz%C3%A4rrap",
        "https://www.op.gg/summoners/las/starseizer",
        "https://www.op.gg/summoners/las/Zyaenn",
        "https://www.op.gg/summoners/las/duketo%20pa",
        "https://www.op.gg/summoners/las/INR%20Manuelift",
        "https://www.op.gg/summoners/las/tomvsjr",
        "https://www.op.gg/summoners/las/ilkartty",
        "https://www.op.gg/summoners/las/miniclip",
        "https://www.op.gg/summoners/las/zaikro",
        "https://www.op.gg/summoners/las/EL%20M%C3%81%20KE%20SUENA"]

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

def calculate_elo(lol_player):
    elo = int(rank_stats['league'][str(lol_player.league)]) + int(rank_stats['division'][str(lol_player.division)]) + lol_player.lp * 0.01
    lol_player.set_elo(elo)
    pass

def order_by_elo():
    tuples_list = []
    for player in players:
        tuples_list.append((player, player.elo))
    result = sorted(tuples_list, key=lambda x: x[1], reverse = True)
    return result


def main():
    for url in urls:
        print(f"leyendo info de : {url}")
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        players.append(info_extracter(html))
    result = []
    for player in players:
        calculate_elo(player)
        result = order_by_elo()
    print(f'\n\n=================================***** ASAMEYA TIERLIST *****==============================\n')
    print("\nel lolero más waton: \n")
    for tuple in result:
        player, _ = tuple
        print(f'        ==================== {player.summoner_name} ====================')
        print(f'{player.show_info()}\n')
    
    print("cierra la wea de programa")
    while True:
        oooooooo = input()
main()