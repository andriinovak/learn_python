class SortedList(list):
	
	def __init__(self, *args):
		super().__init__(*args)
		self.sort()

	def __add__(self, l):
		result = l + self
		return sorted(result)

	def append(self, a1):
		super().append(a1)
		self.sort()

s_list = SortedList([4, 1, 3, 2])
s_list.append(5)
print(s_list)


class NewDict(dict):

	def __getitem__(self, key):
		if not key in self.keys():

#			self[key] = list()
			self.__setitem__(key, [])
			return self[key]
		else:
			return super().__getitem__(key)


n_d = NewDict(one=1, two=2)

n_d['students'].extend(['Alex', 'Ira', 'Bohdan'])
print(n_d.values())
print(n_d.keys())


print(isinstance(n_d, NewDict))


class NewDict(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            inner_list = []
            self[key] = inner_list
            return inner_list


# try:

# except (KeyError, IndexError) as e:



# except Exceptions:
















