class node:
    
    def __init__(self, value):
        self.data = value
        self.next = None
        
class ll:
    
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        
        new_node = node(value)
        
        new_node.next = self.head
        
        self.head = new_node
        
        self.n += 1
        
        
p = ll()
print(len(p))
p.insert_head(10)
p.insert_head(20)
print(len(p))
        