import pyexcel as p
songs_list = p.get_records(file_name = 'itunes_top_songs.xlsx')
chx = int(input('No of song you want to download on Youtube: '))
song = songs_list[chx-1]
from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download([song['Song']+song['Artist']])