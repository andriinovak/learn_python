print('''Dostupni operacii:
	1. +
	2. -
	3. *
	4. /
	5. x^2
	6. x^y''')
oper = input('Operacia:  ')
if oper == ('+'):
	a = input('Pershe chyslo:  ')
	a = float(a)
	b = input('Druge chyslo:  ')
	b = float(b)
	c = a + b
	c = str(c)
	print('Syma: ' + c)
if oper == ('-'):
	a = input('Pershe chyslo:  ')
	a = float(a)
	b = input('Druge chyslo:  ')
	b = float(b)
	c = a - b
	c = str(c)
	print('Vidnimanna: ' + c)
if oper == ('*'):
	a = input('Pershe chyslo:  ')
	a = float(a)
	b = input('Druge chyslo:  ')
	b = float(b)
	c = a * b
	c = str(c)
	print('Mnogenna: ' + c)
if oper == ('/'):
	a = input('Pershe chyslo:  ')
	a = float(a)
	b = input('Druge chyslo:  ')
	b = float(b)
	if b == 0:
		print('Nemoglyvo dilyty na 0')
	else:
		c = a / b
		c = str(c)
		print('Dilenna: ' + c)
if oper == ('x^2'):
	a = input('Vvedit chyslo:  ')
	a = float(a)
	c = a * a
	c = str(c)
	print('Kvadrat chysla: ' + c)
if oper == ('x^y'):
	a = input('Pershe chyslo:  ')
	a = int(a)
	b = input('Druge chyslo:  ')
	b = int(b)
	c = a ** b
	c = str(c)
	print('Stepin chusla: ' + c)

