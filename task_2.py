class Movies:
    def __init__(self):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: {self.movies}'
    
class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'

to_fun_film = Comedy()
to_cry_film = Drama()

print(to_fun_film.add_movie('Большой куш'))
print(to_cry_film.add_movie('Большой куш'))

