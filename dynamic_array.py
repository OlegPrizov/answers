class DynamicArray:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity  
        self.size = 0                   
        self.array = [None] * self.capacity

    def __resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, value):
        if self.size == self.capacity:
            self.__resize()
        self.array[self.size] = value
        self.size += 1

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return self.size
