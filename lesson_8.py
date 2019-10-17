numbers = [0,1,2,3,4,5,6,7,8,9]
for num in numbers:
	if num % 3 != 0:
		continue
	print(f'number: {num}')


words = 'i am happy to learn python end strin'
worlist = words.split()
print(worlist)
maxi = 0
for word in worlist:
	if len(word) >= maxi:
		maxi = len(word)
		maxi_w = word
print(maxi_w)


print(' '.join(worlist))


import random
a = random.randint(1, 10)
astr = str(a)
a1 = astr
a2 = astr + astr
a3 = astr + astr + astr
ans = int(a1) + int(a2) + int(a3)
print(f'{a1} + {a2} + {a3} = {ans}')


words = 'i love maet. also i love isecream'
words_list = words.split()
print(words_list)
a = 0
for word in words_list:
	if word == 'i':
		a = a + 1
print(a)


num = [1,2,1,4,2,1,1,1,5]
print(list(set(num)))
 






