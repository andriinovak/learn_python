class SortedList:

	def __init__(self, your_list):
		self.your_list = your_list

	def sort_list(self):
		self.your_list.sort()
		return self.your_list

	def append_element(self, elem):
		self.your_list.append(elem)
		return self.your_list

	def append_list(self, ap_list):
		self.your_list += ap_list
		return self.your_list

def test_sorted_list(s_list_class):
	errors_list = []

	s_list = s_list_class([1, 3, 5, 6, 4, 2])
	s_list.sort_list()
	expected_list = [1, 2, 3, 4, 5, 6]

	if s_list.your_list != expected_list:
		errors_list.append('List not sorted on creation')

	s_list.append_element(-1)
	s_list.sort_list()
	expected_list.insert(0, -1)

	if s_list.your_list != expected_list:
		errors_list.append('List is not sorted on append')

	s_list.append_list([10, -5])
	s_list.sort_list()
	if s_list.your_list != [-5, -1, 1, 2, 3, 4, 5, 6, 10]:
		errors_list.append('List is not sorted on summation')

	if errors_list:
		print('Please, update SortedList to fix following errors:')
		for err in errors_list: print(err)
	else:
		print('Congrads!')


test_sorted_list(SortedList)


