from urllib.request import urlopen
import re

urls = ["https://www.op.gg/summoners/las/JackSm",
        "https://www.op.gg/summoners/las/fizz%C3%A4rrap",
        "https://www.op.gg/summoners/las/starseizer",
        "https://www.op.gg/summoners/las/Zyaenn",
        "https://www.op.gg/summoners/las/duketo%20pa",
        "https://www.op.gg/summoners/las/INR%20Manuelift",
        "https://www.op.gg/summoners/las/tomvsjr",
        "https://www.op.gg/summoners/las/ilkartty"]

def extract_league_info(html):
    print("hla")
for url in urls:
    print(url)
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    summoner_name = re.search("<span class=\"summoner-name\">(.*)</span>", html).group(1)
    league_html = re.search("<div class=\"tier\">(.*)</div></div></div></div><style data-emotion=\"css 1474l3c\">.css-1474l3c{margin-top:8px;border-radius:4px;background-color:#FFF;background-color:var", html)
    print(league_html.group(1))
    break
