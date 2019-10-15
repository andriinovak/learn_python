l1 = ['ukraine', 'belaus', 'russia', 'america', 'germany', 'serbia', 'finland', 'poland']
for i, l2 in enumerate(l1):
	l1[i] = (l2, i+1)
print(l1)

sev = []

for i in range(0, 71, 7):
	sev.append(i)
print(sev)

sev1 = []
i = 0
while i <=70:
	sev1.append(i)
	i = i + 7
print(sev1)


k = 0
for i in range(10):
	for j in range(3):
		k = k + i
print(k)

import random
poin = 0
while True:
	x = random.randint(0, 10)
	y = random.randint(0, 10)
	print('points: ' + str(poin))
	ans = input(str(x) + '+' + str(y) + '= type q t oquit:  ')
	if ans == 'q':
		break
	elif int(ans) != x+y:
		print('no points for you')
		continue
	print('good job')
	poin = poin + 1
