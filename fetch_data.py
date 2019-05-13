from bs4 import BeautifulSoup
import requests
import time


class FetchData:

    all_lyrics_String = ""
    def __init__(self, link):
        self.link = link

    def __repr__(self):
        return self.link

    def createString(self):
        lyricsDB= []

        source_of_artist = requests.get(self.link).text
        soup1 = BeautifulSoup(source_of_artist, 'lxml')

        list_of_songs = soup1.find('div', attrs={'id': "listAlbum"})
        link_of_songs = list_of_songs.find_all('a')

        for i in link_of_songs:

            try:
                song_link= "https://www.azlyrics.com"+str(i).split('"')[1][2:]
                source_text_of_song = requests.get(song_link).text
                soup2 = BeautifulSoup(source_text_of_song, 'lxml')
                lyrics = soup2.find_all('div', attrs={'class': None})

                lyricsDB=lyricsDB+lyrics[1].text.encode("utf-8").replace("\n"," \n ").split(" ")
            except:
                self.all_lyrics_String = " ".join(lyricsDB)
        return self.all_lyrics_String
