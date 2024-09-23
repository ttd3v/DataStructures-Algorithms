class linkedList:
    root = None
    def __init__(self,value):
        if not self.root and value:
            self.root = [value,None]
    def insert(self,value):
        if not self.root:
            self.root = [value,None]
        else:
            current = self.root
            while current:
                if not current:
                    break
                if current[1] == None:
                    current[1] = [value,None]
                    break
                else:
                    current = current[1]
              
                
    def remove(self,value):
        last = None
        if self.root[0] != value:
            current = self.root
            while current != None:
                if current[0] == value:
                    last[1] = current[1]
                    break
                else:
                    last = current
                    current = current[1]
        else:
            self.root = self.root[1]
    def is_inside(self,value):
        current = self.root
        if not current: return False
        while current:
            if current[0] == value:
                return True
            current = current[1]
        return False
    def __repr__(self) -> str:
        rep = []
        current = self.root
        while current != None:
            rep.append(current[0])
            current = current[1]
        return str(rep)

ll = linkedList(-1)
for i in range(10):
    ll.insert(i)
ll.remove(5)
print(ll)
print(ll.is_inside(5))
