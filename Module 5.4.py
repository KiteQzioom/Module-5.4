Movie1 = {
    "title":"Dune",
    "release":"2021",
    "genre":"Sci-fi"
}

Movie2 = {
    "title":"Cruella",
    "release":"2020",
    "genre":"Animated"
}
Series1 = {
    "title":"Breaking Bad",
    "release":"2008",
    "genre":"Drama",
    "season":1,
    "episode":1
}

Series2 = {
    "title":"Dark",
    "release":"2017",
    "genre":"Sci-fi", 
    "season":1,
    "episode":1
}


class Movie:
    def __init__(self, title, release, genre):
        self.title = title
        self.release = release
        self.genre = genre

        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.title} ({self.release})'

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

Dune = Movie(title=Movie1.get("title"), release=Movie1.get("release"), genre=Movie1.get("genre"))
Cruella = Movie(title=Movie2.get("title"), release=Movie2.get("release"), genre=Movie2.get("genre"))

Breaking_Bad = Series(title=Series1.get("title"), release=Series1.get("release"), genre=Series1.get("genre"), season=Series1.get("season"), episode=Series1.get("episode"))
Dark = Series(title=Series2.get("title"), release=Series2.get("release"), genre=Series2.get("genre"), season=Series2.get("season"), episode=Series2.get("episode"))

x = [Movie1.get("title"), Movie2.get("title"), Series1.get("title"), Series2.get("title")]
y = []
for i in range(0,len(x)):
    y.append(str(x[i]))
print(y)
