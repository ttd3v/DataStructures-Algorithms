class BinarySearchTree:
    def __init__(self):
        self.root = []
    def create_node(self,key,value):
        return [key,value,None,None]
    def insert(self,node):
        if not node:
            return
        if not self.root:
            self.root = node
            return 
        if self.root:
            current = self.root
            while current != None:
                if node[0] > current[0]:
                    if current[3]:
                        current = current[3]
                        continue 
                    else:
                        current[3] = node
                        break
                if node[0] < current[0]:
                    if current[2]:
                        current = current[2]
                        continue 
                    else:
                        current[2] = node
                        break 
    def add(self,key,value):
        self.insert(self.create_node(key,value))
    def find(self,key):
        current = self.root
        while current != None:
            if current[0] == key:
                return current
            if key > current[0]:
                current = current[3]
                continue
            if key < current[0]:
                current = current[2]   
                continue
    def remove(self,key):
        current = self.root
        last = None
        way = 0
        while current != None:
            if current[0] == key:
                node0 = current[2]
                node1 = current[3]
                last[2+way] = None
                self.insert(node0)
                self.insert(node1)
                break
                
            if key > current[0]: 
                last = current
                current = current[3]
                way = 1
                continue 
            if key < current[0]:
                last = current
                way = 0
                current = current[2]    
                continue

bst = BinarySearchTree()
for i in range(2001):
    bst.add(i,f"text[{i}]")
bst.remove(99)
print("--- search\n",f'key(2000) - {bst.find(2000)}',f"\n key(99) - {bst.find(99)}")
