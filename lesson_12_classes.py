class Animals:
	legs = 4
	tail = 1
	animals_attributes = ['tail', 'legs']

	def __init__(self, name):
		self.name = name

	def voice(self):
		print('no voice')


class Dog(Animals):
	
	def voice(self):
		print('gav')

	def run(self):
		print('dog run')

class Cat(Animals):

	def voice(self):
		print('may')

	def climb(self):
		print('cat climb')

	def __add__(self, arg):
		return Cat(f'{self.name}, {arg.name}')

class CatDog(Dog, Cat):
	pass

dogi = Dog('tuzik')
cat_1 = Cat('sharik')
cat_2 = Cat('bobik')
cat_3 = Cat('garfild')
cat_4 = Cat('duren')
print(cat_1.name)
catss = cat_1 + cat_2 + cat_3 + cat_4
print(catss.name)

cat_dog = CatDog('red_one')
cat_dog.voice()
cat_dog.run()
cat_dog.climb()

CatDog.animals_attributes.remove('tail')
print(Animals.animals_attributes)



class Sitizen:

	def sitis(self, town):
		print(f'{self.name} live in {town}')

	def get_country(self, name_country):
		print(f'{self.name} from {name_country}')

class Student:

	def __init__(self, name):
		self.name = name

	def get_student_info(self, university):
		print(f'student {self.name} in {university}')


class Person(Student, Sitizen):
	
	def info_person(self):
		print(f"his name is {self.name}. {stud_1.get_country('ukraine')}, {stud_1.sitis('Rivne')}, {stud_1.get_student_info('rdgu')}")

stud_1 = Person('Bobik')
#print(stud_1.name)
#stud_1.get_country('ukraine')
#stud_1.sitis('Rivne')
#stud_1.get_student_info('RDGU')

stud_1.info_person()


class Citizen:

	def __init__(self, country):
		self.country = country
	def get_country(self):
		print(f'country: {self.country}')

class Student:

	def __init__(self, university, year):
		self.university = university
		self.year = year
	def get_student_info(self):
		print(f'{self.university}, {self.year}')

class Person(Citizen, Student):
	def __init__(self, country, university, year):
		Citizen.__init__(self, country)
		Student.__init__(self, university, year)

our_person = Person('ua', 'univ', 2)
our_person.get_country()
our_person.get_student_info()