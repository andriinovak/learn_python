from random import randint


class PropertiesClass:
    def __init__(self, a):
        self.__hidden = a
        self.__deleted_atrs = []

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, a):
        self.__hidden = randint(0, a)

    @hidden.deleter
    def hidden(self):
        self.__deleted_atrs.append(self.__hidden)
        self.__hidden = None


# prop = PropertiesClass(42)
# print(prop.hidden)
# prop.hidden = 5
# print(prop.hidden)
# del prop.hidden
# print(prop.hidden)
# print(prop._PropertiesClass__deleted_atrs)

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')


class Time:
    def __init__(self, a, b, c):
        self.seconds = a
        self.minutes = b
        self.hours = c


time2 = Time(11, 9, 2012)
print(time2.seconds)
