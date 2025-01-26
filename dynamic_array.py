class DynamicArray:
    def __init__(self, initial_capacity=4):
        """
        Инициализирует динамический массив с заданным начальным размером.
        """
        self.capacity = initial_capacity  # Начальная вместимость массива
        self.size = 0                    # Текущее количество элементов
        self.array = [None] * self.capacity

    def __resize(self):
        """
        Удваивает вместимость массива и переносит старые элементы в новый массив.
        """
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, value):
        """
        Добавляет элемент в массив. Увеличивает размер массива при необходимости.
        """
        if self.size == self.capacity:
            self.__resize()
        self.array[self.size] = value
        self.size += 1

    def __getitem__(self, index):
        """
        Возвращает элемент по индексу.
        """
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        """
        Устанавливает значение элемента по индексу.
        """
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        """
        Возвращает текущее количество элементов в массиве.
        """
        return self.size

    def __str__(self):
        """
        Возвращает строковое представление массива.
        """
        return str([self.array[i] for i in range(self.size)])
