class stack:
    storage = []
    def __init__(self) -> None:
        self.storage = []
    def add(self,value):
        self.storage.append(value)
    def pop(self):
        return self.storage.pop(len(self.storage)-1)
    def read(self):
        return self.storage[len(self.storage)-1]
    def clear(self):
        self.storage = []
    def __len__(self):
        return len(self.storage)
    def __repr__(self) -> str:
        return str(self.storage)
    def __str__(self) -> str:
        return str(self.storage)
    
stack_ = stack()
