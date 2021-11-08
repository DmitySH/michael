class Film:
    def __init__(self, title, year):
        self._year = year
        self._title = title

    def __sort_key(self):
        return round(self._year / len(self._title), 3)

    def __str__(self):
        return f'Sort key is {self.__sort_key()}'

    def __lt__(self, other):
        return self.__sort_key() < other.__sort_key()


class Gaming(Film):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.__director = director

    def __str__(self):
        return f'Gaming {self._title}, year of film {self._year}, by {self.__director}.' \
               f' {super().__str__()}'


class Cartoon(Film):
    def __init__(self, title, year, created_as):
        super().__init__(title, year)
        if created_as != 'drawn' and created_as != 'dollhouse' and created_as != 'plasticine':
            raise ValueError('Incorrect type of creation')
        self.__created_as = created_as

    def __str__(self):
        return f'Cartoon {self._title}, year of film {self._year}, was {self.__created_as}.' \
               f' {super().__str__()}'


class Documentary(Film):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.__duration = duration

    def __str__(self):
        return f'Documentary {self._title}, year of film {self._year}, {self.__duration} long.' \
               f' {super().__str__()}'
