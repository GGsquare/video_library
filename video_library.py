import random

##########---Class---##########

class Movies:
    def __init__(self, type,  title, year, genre, number_of_plays):
        self.type = type
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays

    def __str__(self):
        return f'{self.type}: {self.title} {self.year}, \nliczba odtworzeń: {self.number_of_plays}'
    #@property
    #def __str__(self):
        #return f'{self.type}: {self.title} {self.year} {self.genre} \nliczba odtworzeń: {self.number_of_plays}'

    def __repr__(self):
        return f"Movies(title={self.title} year={self.year} genre={self.genre} number_of_plays={self.number_of_plays})"

    def play(self, step=1):
            self.number_of_plays += step
            print(f'Liczba odtworzeń:{self.type}u {self.title} to: {self.number_of_plays}')

class Series(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.type}: {self.title} S{str(self.season_number).zfill(2)}E{str(self.episode_number).zfill(2)}, \nliczba odtworzeń: {self.number_of_plays}'

##########---functions---##########

def search():
    a = input("Tu wpisz szukany tytuł:")
    x = int(len(biblioteka))
    for i in range(x):
        if a == biblioteka[i].title:
            a = f'{biblioteka[i].title} {biblioteka[i].year} {biblioteka[i].genre}, \nliczba odtworzeń: {biblioteka[i].number_of_plays}'
            print(a)

def generate_views():
    x = random.choice(biblioteka)
    x.play(random.randint(1,100))
    return f''

def auto_views_gen():
    for z in range(10):
        z = generate_views()
        print(z)

def get_movies():
    movies =[]
    x = int(len(biblioteka))
    for i in range(x):
        if biblioteka[i].type == "Film":
            print(biblioteka[i], sep="\n")
            movies.append(biblioteka[i])

def get_series():
    series =[]
    x = int(len(biblioteka))
    for i in range(x):
        if biblioteka[i].type == "Serial":
            print(biblioteka[i], sep="\n")
            series.append(biblioteka[i])

def top_titles():
    number_of_plays_m = []
    number_of_plays_s = []
    a = input("Wpisz 'Film' dla top filmy lub 'Serial' dla top seriali:")
    if a == "Film":
        x = int(len(biblioteka))
        for i in range(x):
            if biblioteka[i].type == "Film":
                number_of_plays_m.append(biblioteka[i])
                by_views = sorted(number_of_plays_m, key=lambda x: x.number_of_plays)
                by_views.reverse()
        for x in range(len(by_views)):
            print(by_views[x])
    elif a =="Serial":
        x = int(len(biblioteka))
        for i in range(x):
            if biblioteka[i].type == "Serial":
                number_of_plays_s.append(biblioteka[i])
                by_views = sorted(number_of_plays_s, key=lambda x: x.number_of_plays)
                by_views.reverse()
        for x in range(len(by_views)):
            print(by_views[x])

##########---Class objects---##########

movie1 = Movies(type = "Film", title = "Pulp Fiction", year = 1994, genre = "Criminal/Drama", number_of_plays = 0)
movie2 = Movies(type = "Film", title = "Reservoir Dogs", year = 1992, genre = "Criminal/Drama", number_of_plays = 0)
movie3 = Movies(type = "Film", title = "Jackie Brown", year = 1997, genre = "Criminal/Drama", number_of_plays = 0)
movie4 = Movies(type = "Film", title = "Four Rooms", year = 1995, genre = "Comedy", number_of_plays = 0)
movie5 = Movies(type = "Film", title = "Kill Bill", year = 2003, genre = "Action/Criminal", number_of_plays = 0)

serie1 = Series(type = "Serial", title = "The Simpsons", year = 1990, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 20, season_number = 6)
serie2 = Series(type = "Serial", title = "Family Guy", year = 1999, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 21, season_number = 22 )
serie3 = Series(type = "Serial", title ="Rick and Morty", year = 2013, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 6, season_number = 5)
serie4 = Series(type = "Serial", title = "American Dad", year = 2005, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 18, season_number = 18)
serie5 = Series(type = "Serial", title ="Archer", year = 2009, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 15, season_number = 12)

biblioteka = [movie1,movie2, movie3, movie4, movie5, serie1, serie2, serie3, serie4, serie5]

##########---Testing area---##########
text = "Biblioteka filmów i seriali."
print("\n",text.center(58, '-'), "\n")
for i in biblioteka:
    print(i)

print("\nSame filmy\n")
get_movies()

print("\nSame seriale\n")
get_series()

print("\nRęczny generator liczby odtworzeń dla danego filmu")
movie1.play(15)
print('\nTo samo tylko dla serialu')
serie5.play(9)

print("\nAutomatyczny generator odtworzeń dla dowolnego tytułu")
generate_views()
print("\nAutomatyczny generator odtworzeń dla 10 dowolnych tytułów")
auto_views_gen()

print("\nWyszukiwarka")
search()

top_titles()

