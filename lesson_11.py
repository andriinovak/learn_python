from random import randint

class movie:
	def __init__(self, title, genre = 'action'):
		self.title = title
		self.budget = randint(100, 1000)
		self.genre = genre
		self.__director = 'roman'
		self.has_seen = False

	def print_movie(self, count = 1):
		for i in range(count):
			print(f'movie: {self.title}, (${self.budget}), seen?:  {self.has_seen}')

	def watch(self):
		self.has_seen = True



joker_movie = movie('joker', genre = 'drama')
pirate_movie = movie('the pirates of caribbian')


movies = [
	joker_movie,
	pirate_movie,
	movie('friends', genre = 'sitcom'),
	movie('green elephant', genre = 'comedy'),
	movie('this is as', genre = 'drama')
	]

joker_movie.watch()
pirate_movie.watch()

for movie in movies:
	if movie.has_seen:
		movie.print_movie()


#joker_movie.print_movie()
#joker_movie.budget = 100000
#joker_movie.genre = 'drama, thriller'
#joker_movie.print_movie()

