class Car:
	doors = 4
	engine = 1
	engine_type = 'fuel'
	driver = 1

	def __init__(self, name, speed, fuel_use):
		self.name = name
		self.speed = speed
		self.distance = 0
		self.fuel_use = fuel_use
		self.fuel_in_bak = 0

	def __repr__(self):
		return f'Car:  ({self.name}), speed:  {self.speed}, distance:  {self.distance}, {self.engine_type}'

	def __str__(self):
		return f'Car:  {self.name}, speed:  {self.speed}, distance:  {self.distance}, {self.engine_type}'

	def drive(self, distance, fuel_in_bak):
		self.distance += distance
		hours = distance / self.speed
		fuel_lost = fuel_in_bak - distance / 100 * self.fuel_use
		return f'{self.name} drove {self.distance} km in {hours} h., {fuel_lost}, use for 100km {self.fuel_use} l of fuel.' 

	def before_drive(self, data):
		print(data)

	def __add__(self, other_car):
		return f'{car_1.name}, {other_car}'

class Electro_Car(Car):
	engine_type = 'electro'

	def __init__(self, name, speed, fuel_use, people):
		super().__init__(name, speed, fuel_use)
		self.people = people


	def drive(self, distance, battery):
		super().before_drive('good by')
		self.distance += distance
		battery_lost = battery - distance / 100 * self.fuel_use
		return f'{self.name} drove {distance}, and have battery: {battery_lost}'

car_1 = Car('bmv', 120, 8)
car_2 = Car('mazda', 90, 7)
car_3 = Electro_Car('nissan leaf', 100, 10, 5)
#print(car_1.drive(600))
#print(car_2.drive(450))
#print(car_3.drive(700))

print(car_1.drive(600, 50))
print(car_2.drive(450, 40))
print(car_3.drive(700, 85))

print(car_1 + car_2)


