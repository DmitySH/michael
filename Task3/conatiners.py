import random
import string

from entities.films import *


class Container:
    def __init__(self):
        self.__max_size = 100000
        self.__list = list()

    def input_file(self, path):
        with open(path, 'r') as file:
            for line in file:
                if self.__max_size <= len(self.__list):
                    raise IndexError('Too much elements')
                words = line.split()
                if len(words) != 4:
                    raise ValueError('Incorrect arguments')
                if int(words[0]) == 1:
                    self.__list.append(Gaming(words[1], int(words[2]), words[3]))
                elif int(words[0]) == 2:
                    self.__list.append(Cartoon(words[1], int(words[2]), words[3]))
                elif int(words[0]) == 3:
                    self.__list.append(Documentary(words[1], int(words[2]), int(words[3])))
                else:
                    raise ValueError('Incorrect number of movie')

    def write_file(self, path):
        with open(path, 'w') as file:
            file.write(self.__str__())

    def random_in(self, num):
        if num > self.__max_size:
            raise IndexError('Too much elements')
        for i in range(num):
            k = random.randint(1, 3)
            if k == 1:
                self.__list.append(
                    Gaming(generate_random_string(random.randint(5, 25)), random.randint(1900, 2021),
                           generate_random_string(random.randint(3, 20))))
            elif k == 2:
                t = random.randint(1, 3)
                if t == 1:
                    typ = 'drawn'
                elif t == 2:
                    typ = 'dollhouse'
                else:
                    typ = 'plasticine'
                self.__list.append(
                    Cartoon(generate_random_string(random.randint(5, 25)), random.randint(1900, 2021), typ))
            else:
                self.__list.append(
                    Documentary(generate_random_string(random.randint(5, 25)), random.randint(1950, 2021),
                                random.randint(50, 270)))

    def __str__(self):
        res = 'Container now: \n'
        i = 1
        for film in self.__list:
            res += '{}: {}\n'.format(str(i), film.__str__())
            i += 1
        return res

    def __swap(self, i, j):
        self.__list[i], self.__list[j] = self.__list[j], self.__list[i]

    def __heapify(self, end, i):
        left = 2 * i + 1
        right = 2 * (i + 1)
        max_element = i
        if left < end and self.__list[i] < self.__list[left]:
            max_element = left
        if right < end and self.__list[max_element] < self.__list[right]:
            max_element = right
        if max_element != i:
            self.__swap(i, max_element)
            self.__heapify(end, max_element)

    def heap_sort(self):
        end = len(self.__list)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            self.__heapify(end, i)
        for i in range(end - 1, 0, -1):
            self.__swap(i, 0)
            self.__heapify(i, 0)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
