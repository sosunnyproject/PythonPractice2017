from bs4 import BeautifulSoup
import requests
import re

#http
url_2 ="http://www.billboard.com/charts/year-end/2016/digital-songs"
r = requests.get(url_2)

#saving html code that is translated via BeautifulSoup package
music = BeautifulSoup(r.text, "html5lib")

billboard = []
song = music('h1', 'ye-chart__item-title')
artist = music('a', 'ye-chart__item-subtitle-link')
song_num = len(song)
artist_num = len(artist)
#returns 75 length

yechart_songs = song_num + 1
yechart_artists = artist_num + 1
print("total number of songs: ", yechart_songs)
print("total number of artists: ", yechart_artists)
#returns 76, total 76 items

songs = music.findAll('h1', 'ye-chart__item-title')
for s in songs:
    lst = s.text.strip("\n")
    print(lst)

"""-----------------------------------------------"""

divs = music('div', 'ye-chart__item-primary')
divs_num = len(divs)

def is_Justin(div):
    justin = div('a', 'ye-chart__item-subtitle-link')
    #jb = re.search(r"\bJustin Bieber\b", justin_text)
    return (len(justin) == 1 and
            justin[0].text.strip().startswith("Justin Bieber"))
jLen = len([div for div in divs if is_Justin(div)])
print(jLen, "of Justin Bieber songs are on 2016 billboard year-end list")
#change if to if not, if you want to exclude JB

#probably not working
def song_info(div) :
    ranking = div.find("div", "ye-chart__item-rank").text
    title = div.find("h1", "ye-chart__item-title").text
    artist = div.find("a", "ye-chart__item-subtitle-link").text

    return {
        "ranking" : ranking,
        "artist" : artist,
        "title" : title
    }

#notworking
JBsongs = []
for div_num in range(1, divs_num + 1):
    music = BeautifulSoup(requests.get(url_2).text, 'html5lib')
    for div in music ('div', 'ye-chart__item-primary'):
        if is_Justin(div):
            JBsongs.append(song_info(div))
