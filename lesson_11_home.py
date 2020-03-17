class Car():

	def __init__(self, brand, model, year, color):
		self.brand = brand
		self.model = model
		self.year = year
		self.color = color
		self.total_driven_km = 0

	def repaint(self, color):
		self.color = color

	def drive(self, km_drive):
		self.total_driven_km += km_drive
car_1 = Car('Volvo', 'V90', 2016, 'white')
car_2 = Car('Ford', 'Focus', 2014, 'grey')

