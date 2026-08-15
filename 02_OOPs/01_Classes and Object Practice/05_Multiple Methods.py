#  Class Methods

class Playlist:

    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f'{song} Song is Added')

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} removed")

    def show_songs(self):

        print(f"playlist '{self.name} <3'")

        for song in self.songs:
            print(f'- {song}')

s = Playlist('love')
s.add_song('sru')
s.add_song('raj')
s.add_song('rs')
s.add_song('rsrs')
s.show_songs()
s.remove_song('rs')
s.show_songs()