a = []
b = list()
print(a)
print(b)
t1 = (1,2,3)
l1 = list(t1)
print(l1)
l1.append(22)
print(l1)
del(l1[0])
print(l1)
l1.append(22)
l1.append(22)
l1.append(22)
print(l1)
l1.extend([5])
print(l1)
l2 = [45,46]
l1.append(l2)
print(l1)
print(l1[-1])
print(l1[-1][0])
l1.append((42,43))
print(l1)
print(l1[-1][0])
l2 = l1.copy()
print(l2)
l2[1] = 'python'
print(l2)
print(l1)
l1 = [5,2,1,-4,3]
l1.sort()
print(l1)
l1.insert(1,45)
print(l1)
print(l1.pop(2))
l1.reverse()
print(l1)
tuple(l1)
print(l1)
print(l1.count(5))
print(l1.index(5))
print(set(l1))
lis1 = [1,2,3,4]
s1 = set(lis1)
print(s1)
s2 = {3,4,5}
print(s2)
import random
print(dir(random))
print(random.randint(1,10))
from random import randint
print(randint(1,10))
l1 = []
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
l1.append(randint(1,10))
print(l1)
l2 = []
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
l2.append(randint(1,10))
print(l2)
print(l1 + l2)
l1.extend(l2)
print(l1)
print(set(l1))
s1 = set(l1)
print(len(s1))
dict()
d1 = {'user1':['apple','banana']}
print(d1)
d2 = {'user1':['apple','banana'], 'user2':'123'}
print(d2)
dir(d1)
print(d1['user1'])
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.pop('user1'))
print(d2)
print(d2.get('user2'))
d2['user2'] = ['123', '456']
print(d2)
bir = dict()
print(bir)
bir['july'] = list()
print(bir)
bir['july'].append('stepan')
print(bir)
bir['july'].append('ira')
print(bir)
bir['jan'] = ['andrii']
print(bir)
bir['august'] = ['vasyl']
print(bir)
print(bir.keys())
print(bir.values())
print(bir.items())
