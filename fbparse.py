'''
    Facebook page parser
'''


import re
import requests

example = \
'''
<script>...
"require":[["PagesLikesTab","renderLikesData",["m_0_6"],[{"__m":"m_0_6"},1412578800,[38899,36849,42248,49295,50444,43025,39831,39251,29268,29336,31095,33199,0,0],89149451]],
["PagesLikesTab","renderPTATData",["m_0_7"],[{"__m":"m_0_7"},874095]],["PagesTimelineChaining","init",["m_0_8"],[{"__m":"m_0_8"},{"pageID":"40796308305"}]]]},"css":["EzzkY","XVpqc","96uQ6","KP0Yf","\/Pdzc","tUdUf"],"resource_map":{"Zml5X":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/ye\/r\/zKQrlpTrVYO.js"},"PQEtn":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yh\/r\/bUYR32ipIKr.js"},"rKCxx":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yD\/r\/HU38Lv5q9WI.js"},"EtJWZ":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yz\/r\/6jmzxEHdTUr.js"},"DV6bT":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/ye\/r\/xGtradaduSJ.js"},"Xya3V":{"type":"js","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yl\/r\/oGCT3h046X7.js"},"EzzkY":{"type":"css","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yp\/r\/F6NddDA2EU7.css"},"tUdUf":{"type":"css","crossOrigin":1,"src":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/yj\/r\/cpdDxhicHRc.css"}},"ixData":{"\/images\/hubble\/info\/info-flat_s.png":{"sprited":false,"uri":"https:\/\/fbstatic-a.akamaihd.net\/rsrc.php\/v2\/y8\/r\/KyGlu5vIHjU.png","width":13,"height":13}},"js":["v9pRR","0jyeX","RoWGo","wPIWf","upUfw","Zml5X","PQEtn","rKCxx","EtJWZ","DV6bT","V\/3oy","Xya3V"],"displayJS":["PQEtn","0jyeX","v9pRR","RoWGo","rKCxx","EtJWZ","DV6bT","V\/3oy","Xya3V","wPIWf"],"id":"PagesLikesTabController_40796308305","phase":1})</script>
'''
likes_re = re.compile(r'\["PagesLikesTab",.+?(\d+)\]\]', re.MULTILINE)

HOST = 'https://www.facebook.com/'
#page = 'samsung' # samsung cocacola
#url = HOST + page + '/likes'
headers = {"Accept-Language": "en-US"}


def likes_shares_parse(page):
    url = HOST + page + '/likes'
    r = requests.get(url, headers=headers)

    if not r.status_code == 200:
        raise Exception("Page not found")

    html = r.content
    #print html
    #exit()

    arr = likes_re.findall(html)
    #print arr

    if not len(arr) == 2:
        raise Exception("Parse error, or no likes on the page")

    #likes = arr[0]
    #talking_about = arr[1]

    return {"likes": arr[0], "shares": arr[1]}


if __name__ == "__main__":
    print likes_shares_parse('samsung')




