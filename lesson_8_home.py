

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c = []
b = [i if i % 2 == 0 else c.append(i) for i in a]
d = [ind for ind in b if ind != None]
print(d)
print(b)
print(c)


slovnyk = {}
string = 'i love isecream also i love beetroot'
string_list = string.split()
string_list_1 = {word : string_list.count(word) for word in string_list}
print(string_list_1)
for word in string_list:
	slovnyk[word] = string_list.count(word)
print(slovnyk)


a = [1, 3, 1, 6, 1]
print(a.count(1))


b = [1, 2, 4, 1, 3, 2, 4, 45, 112, 56]
print(list(set(b)))


b = [1, 2, 4, 1, 3, 2, 4]
c = []
for di in b:
	if di not in c:
		c.append(di)
print(c)


n = input('enter digit:  ')
suma = 0
for i in range(0, len(n)):
	suma = suma + int(n[i])
print(suma)


x = input('enter digit:  ')
factor = 1
for i in range(1, int(x)+1):
	factor = factor * i
print(factor)




x = input('enter digit:  ')
di = {}
for i in range(1, int(x) + 1):
	cvad = i * i
	di[i] = cvad
print(di)





