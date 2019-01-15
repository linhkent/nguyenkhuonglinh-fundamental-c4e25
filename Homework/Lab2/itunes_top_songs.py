url = 'https://www.apple.com/itunes/charts/songs/'
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
com = urlopen(url)
rawdata = com.read()
content = rawdata.decode('utf8')
soup = BeautifulSoup(content,'html.parser')
ul = soup.find('ul','')
li_list = ul.find_all('li')
songs_list = []
n = 1
for li in li_list:
    name = li.h3.string
    artist = li.h4.string
    song = {
        'No' : n,
        'Song' : name,
        'Artist' : artist
    }
    songs_list.append(OrderedDict(song))
    n += 1
import pyexcel
pyexcel.save_as(records=songs_list, dest_file_name="itunes_top_songs.xlsx")