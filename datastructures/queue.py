class queue:
    storage = []
    def __init__(self) -> None:
        self.storage = []
    def pop(self):
        return self.storage.pop(0)
    def add(self,value) -> None:
        self.storage.append(value)
    def clear(self) -> None:
        self.storage = []
    def read(self):
        return self.storage[0]
    def __len__(self):
        return len(self.storage)
    def __repr__(self) -> str:
        return str(self.storage)
    def __str__(self) -> str:
        return str(self.storage)
    
queue_ = queue()
