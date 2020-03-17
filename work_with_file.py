with open('weekdays.txt') as week_file:
	weekdays = [day.rstrip() for day in week_file.readlines()]
print(weekdays)


#username = input('whats your name?:  ')
#print(help(open))
#with open('our_file.txt', 'a') as file_to_read:
#	file_to_read.write('string1')

#with open('our_file.txt') as file_to_read:
#	text = file_to_read.read()

#print(text)


#my_file = open('our_file.txt', 'r+')
#content = my_file.read()
#content = content + 'hello world'
#print(my_file.name)
#my_file.write(content)
#my_file.close()
#print(content)


#try:
#except:
#print('error')
input_val = 2
a = 20
try:
	a = 20 / int(input_val)
except ZeroDivisionError:
	print('error')
print(a)





