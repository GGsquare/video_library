from cProfile import run
from filecmp import cmp
from webbrowser import get
import random

class Movies:
    def __init__(self, typ,  title, year, genre, number_of_plays):
        self.typ = typ
        self.title = title
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays
    def __str__(self):
        return f'{self.typ}: {self.title} {self.year}'
    def __repr__(self):
        return f"Movies(title={self.title} year={self.year} genre={self.genre} number_of_plays={self.number_of_plays})"
    def play(self, step=1):
            self.number_of_plays += step
            print(f'Liczba odtworzeń:{self.typ}u {self.title} to: {self.number_of_plays}')
    """def get_movie(self):
        for movies in biblioteka:
                print(movies)
        print(f'{sorted(movies, key=lambda m: m.title)}')"""
    def search(self):
        self.title = input("Tu wpisz tytuł filu:")
        return print(f'{self.title} {self.year} {self.genre}, \nliczba odtworzeń: {self.number_of_plays}')
    #def search(self):
        #if self.title == input(f'Movie title:'):
            #return print(f'{self.title} {self.year} {self.genre}, \nliczba odtworzeń: {self.number_of_plays}')
    def generate_views(self):
        x = random.choice(biblioteka)
        x.play(random.randint(1,100))
        return f''
    def auto_views_gen(self):
        for z in range(10):
            z = movie1.generate_views()
            print(z)
    def top_titles(self):
        pass

        #return f'Najpopularniejszy tytuł to: {y}, był odtworzony: {self.number_of_plays} razy.'

class Series(Movies):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    def __str__(self):
        return f'{self.typ}: {self.title} S{str(self.season_number).zfill(2)}E{str(self.episode_number).zfill(2)}'
    """def get_serie(self):
        for a in biblioteka:
            a == Series
            print(a)
            print(f'{sorted(biblioteka, key=lambda s: s.title)}')"""
    def search(self):
        self.title = input("Tu wpisz tytuł serialu:")
        return print(f'{self.title} {self.year} {self.genre}, \nliczba odtworzeń: {self.number_of_plays}')
    
movie1 = Movies(typ = "Film", title = "Pulp Fiction", year = 1994, genre = "Criminal/Drama", number_of_plays = 5)
movie2 = Movies(typ = "Film", title = "Reservoir Dogs", year = 1992, genre = "Criminal/Drama", number_of_plays = 0)
movie3 = Movies(typ = "Film", title = "Jackie Brown", year = 1997, genre = "Criminal/Drama", number_of_plays = 0)
movie4 = Movies(typ = "Film", title = "Four Rooms", year = 1995, genre = "Comedy", number_of_plays = 0)
movie5 = Movies(typ = "Film", title = "Kill Bill", year = 2003, genre = "Action/Criminal", number_of_plays = 0)

serie1 = Series(typ = "Serial", title = "The Simpsons", year = 1990, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 20, season_number = 6)
serie2 = Series(typ = "Serial", title = "Family Guy", year = 1999, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 21, season_number = 22 )
serie3 = Series(typ = "Serial", title ="Rick and Morty", year = 2013, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 6, season_number = 5)
serie4 = Series(typ = "Serial", title = "American Dad", year = 2005, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 18, season_number = 18)
serie5 = Series(typ = "Serial", title ="Archer", year = 2009, genre = "Animation/Comedy", number_of_plays = 0, episode_number = 15, season_number = 12)
biblioteka = [movie1,movie2, movie3, movie4, movie5, serie1, serie2, serie3, serie4, serie5]


#by_movies = sorted(biblioteka, key=lambda e: e.title)
#print(by_movies)

#by_serie = sorted(biblioteka, key=lambda a: a.typ)
#print(by_serie)
print("\nWyszukiwarka")
serie1.search()
movie2.search()
print("\nRęczny generator liczby odtworzeń")
movie1.play(15)
print('\nto samo tylko dla seriali')
serie5.play(9)


#print(serie1.get_serie()
print("\nAutomatyczny generator odtworzeń dla wybranego filmu")
movie1.generate_views()
print("\nAutomatyczny generator randomowych tytułów")
movie1.auto_views_gen()

#movie1.top_titles()
