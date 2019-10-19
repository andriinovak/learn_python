shop = {}
shop['apple'] = {'price': 10, 'count': 2}
shop['banana'] = {'price': 20, 'count': 25}
shop['carrot'] = {'price': 100, 'count': 0}
shop['cheryy'] = {'price': 1, 'count': 10}
shop['milk'] = {'price': 30, 'count': 300}

#for name in shop.keys():
#	if shop[name]['price'] > 10:
#		print(name, shop[name]['price'])
#	if props['count'] < 5:
#		print(name, props['count'])
#print(shop)


a = [name for name in shop.keys() if shop[name]['price'] > 10]
b = [name for name in shop.keys() if shop[name]['count'] < 5]
for i in a:
	print(i)
for i in b:
	print(i)



suma = 0
for name in shop.keys():
	suma = suma + shop[name]['count']
print(suma)


suma_1 = sum(shop[name]['count'] for name in shop.keys())
print(suma_1)


exps = []
exps.append({'one' : 5, 'two' : 10, 'action' : '+'})
exps.append({'one' : 10, 'two' : 2, 'action' : '-'})
#for el in exps:
#	if el['action'] == '+':
#		print(el['one'] + el['two'])
#	else:
#		print(el['one'] - el['two'])

exps.append({'one' : 1, 'two' : 14, 'action' : '*'})
exps.append({'one' : 2, 'two' : 7, 'action' : '/'})

for el in exps:
	if el['action'] == '+':
		print(el['one'] + el['two'])
	if el['action'] == '-':
		print(el['one'] - el['two'])
	if el['action'] == '*':
		print(el['one'] * el['two'])
	else:
		print(el['one'] / el['two'])


new_shop = []
for i in shop.keys():
	z = {'name' : i, 'price' : shop[i]['price'], 'count' : shop[i]['count']}
	new_shop.append(z)
	

print(new_shop)


