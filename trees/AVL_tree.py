class avl_node:
    key = None
    value = None
    height = 0
    balance = 0
    leftNode = None
    rightNode = None
    bottom_limit = 5
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def insert(self,node ):
        current = self
        if current.key > node.key:
            if not current.leftNode:
                current.leftNode = node  
                return
            if current.leftNode:
                ##print(current.key,">",current.leftNode.key," | ",node.key)
                current.leftNode.insert(node)
                return
        if current.key < node.key:
            if not current.rightNode:
                current.rightNode = node   
                return
            if current.rightNode:
                ##print(current.key,">",current.rightNode.key," | ",node.key)
                current.rightNode.insert(node)
                return      
    def get_balance(self):
        balance = 0
        if self.leftNode:
            balance += 1 
        if self.rightNode:
            balance -= 1
        
        rightBottom = None
        leftBottom = None
        current = self
        if current.rightNode:
            current = self.rightNode
            for i in range(self.bottom_limit):
                if current and current.rightNode:
                    balance -= 1
                    current = current.rightNode
                    rightBottom = current
                else:
                    break
        if current.leftNode:
            current = self.leftNode
            for i in range(self.bottom_limit):
                if current and current.leftNode:
                    balance += 1
                    current = current.leftNode
                    leftBottom = current
                else:
                    break
        if leftBottom: balance += leftBottom.get_balance()
        if rightBottom: balance += rightBottom.get_balance()

        self.balance = balance
        return balance
    
    
    def __str__(self) -> str:
        return "({},({}),({}),({}) |".format(self.key,self.balance,self.leftNode,self.rightNode)

class avl_tree:
    root = None
    balance = 0
    def __init__(self) -> None:
        pass
    def remove(self,key):
        last = None
        current = self.root
        while current != None:
            if current.key == key:
                left = current.leftNode
                right = current.rightNode
                current.leftNode = None
                current.rightNode = None
                if current == self.root:
                    self.root = None
                    if left: self.insert(left)
                    if right: self.insert(right)
                if last:
                    if last.leftNode == current:
                        last.leftNode = None
                    if last.rightNode == current:
                        last.rightNode = None
                    if left: self.insert(left)
                    if right: self.insert(right)
                break
            if current.key > key:
                current = current.leftNode
                continue
            if current.key < key:
                current = current.rightNode
                continue
        self.make_stable()
    def add(self,key,value):
        node = avl_node(key,value)
        self.insert(node)
    def search(self,key):
        current = self.root
        while current != None:
            if current.key == key:
                return current
            if current.key > key:
                current = current.leftNode
                continue
            if current.key < key:
                current = current.rightNode
                continue
        return None
    
    def insert(self,node) -> None:
        if not node:
            return
        if not self.root:
            self.root = node
            self.make_stable()
            return None
        if self.root:
            self.root.insert(node)
            self.make_stable()
            return None
    def make_stable(self):
        if self.root:
            self.balance = self.root.get_balance()
            root = self.root
            if self.balance < -1:
                rootNodes = [root.leftNode,root.rightNode]
                rootBox = root
                self.root = None
                root.leftNode = None
                root.rightNode = None
                self.root = rootNodes[1]
                self.insert(rootBox)
                self.insert(rootNodes[0])
            if self.balance > 1:
                rootNodes = [root.leftNode,root.rightNode]
                rootBox = root
                self.root = None
                root.leftNode = None
                root.rightNode = None
                self.root = rootNodes[0]
                self.insert(rootBox)
                self.insert(rootNodes[1])
            if self.balance < -1 or self.balance > 1:
                self.make_stable()

            ## Insert again
    def visual(self) -> str:
        right_way = []
        left_way = []
        
        current = self.root
        while current != None:
            left_way.append(current.key)
            current = current.leftNode
        current = self.root
        while current != None:
            right_way.append(current.key)
            current = current.rightNode
    def __str__(self):
        return f"avl_tree({self.root})"
    def __len__(self):
        if self.root:
            return len(self.root)
        else:
            return 0


avlt = avl_tree()
