a = [1, 3, 1, 6, 1]
print(a.count(1))


b = [1, 2, 4, 1, 3, 2, 4]
print(list(set(b)))


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


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [a[i] for i in range(0, len(a)) if a[i] % 2 == 0]
print(b)


x = input('enter digit:  ')
di = {}
for i in range(1, int(x) + 1):
	cvad = i * i
	di[i] = cvad
print(di)





