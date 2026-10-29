class Song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration

class Playlist:
    def __init__(self,name,songs):
        self.name=name
        self.songs=songs

    def add_song(self,song):
        self.songs.append(song)

    def get_total_duration(self):
        duration=0
        for song in self.songs:
            duration+=song.duration
        dmins=duration//60
        dsecs=duration%60
        return(f'{dmins}:{dsecs}')

    def find_by_artist(self,artist_name):
        found=False
        for song in self.songs:
            if song.artist==artist_name:
                print(song.title)
                found=True
        if not found:
            print("No songs by this artist found in this playlist.")

    def print_playlist(self):
        print(self.name.upper())
        for song in self.songs:
            print(f'{song.title}, {song.artist}')

    def load_songs(self,filename):
        songs=[]
        with open(filename, "r") as l:
            songs=l.readlines()

        for line in songs:
            line=line.strip()
            nsl=line.split(",")
            new_song=Song(nsl[0],nsl[1],int(nsl[2]))
            self.add_song(new_song)

