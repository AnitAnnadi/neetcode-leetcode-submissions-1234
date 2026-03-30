class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1;
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        tmpArr = [0] * self.capacity

        for i, num in enumerate(self.arr):
            tmpArr[i] = num
        
        self.arr = tmpArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
