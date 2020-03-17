print((lambda x,y : x + y)(2,3))

name = 'ira'
second_name = 'bogdan'

def get_my_name(name):
	print(name)
	names = ['oleg', 'homan']	
	for index, name in enumerate(names):
		print(name)
	print(index)
	print(name)
	
get_my_name(name)

kind = 'homework'
def print_lesson():
	title = 'lesson function scope'
	return {
		'title' : title,
		'kind' : kind
	}


print(print_lesson())

#global
#nonlocal