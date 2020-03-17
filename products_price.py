products_with_price = {
		'SMART WATCH': 550,
		'PHONE' : 1000,
		'PLAYSTATION': 500,
		'LAPTOP' : 1550,
		'MUSIC PLAYER' : 600,
		'TABLE' : 400
		}

def products_price(data):
	user_input_price = input('input your price:   ')
	user_input_price = int(user_input_price)
	list_of_prices = []
	products_list = []
	for item in data.keys():
		if data[item] <= user_input_price:
			products_list.append(item)
	print(products_list)


products_price(products_with_price)