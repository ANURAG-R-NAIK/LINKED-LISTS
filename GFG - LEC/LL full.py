class node:
    
    def __init__(self, value):
        self.data = value
        self.next = None
    
class LL:
    
    def __init__(self):
        self.head = None
        
    def insert_head(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert_end(self, value):
        if self.head == None:
            return node(value)
            
        new_node = node(value)
        
        cur = self.head
        
        while cur.next != None:
            cur = cur.next
        
        cur.next = new_node
        
    def print_value(self):
        cur = self.head
        
        while cur != None:
            print(cur.data, "->", end = " ")
            cur = cur.next
            
    def insert_middle(self, value, pos):
        if pos == 1:
            new_node.next = self.head
            return new_node
        cur = self.head
        ind = 1
        
        while cur.next != None:
            if ind == pos - 1:
                break
            cur = cur.next
            ind += 1
        
        new_node = node(value)
        new_node.next = cur.next
        cur.next = new_node
        
    def delete_head(self):
        if cur == None:
            print("empty LL")
        cur = self.head
        
        self.head = cur.next
        
    def last_delete(self):
        cur = self.head
        
        if cur == None:
            print("emty LL")
            
        if cur.next == None:
            self.head = None
        
        while cur.next.next != None:
            cur = cur.next
        
        cur.next = None
        
    def sorted_insert(self, value): # for this the input LL must be sorted in order
        cur = self.head
        new_node = node(value)
        
        if cur == None:
            print("empty LL")
            return
        
        while cur.next != None:
            if cur.data < value and cur.next.data > value:
                break
            cur = cur.next 
            
        if cur.next == None and cur.data < value:
            cur.next = new_node
        
        new_node.next = cur.next
        cur.next = new_node
        
    def rev_list(self):
        stack = []
        
        cur = self.head
        
        while cur is not None:
            stack.append(cur.data)
            cur = cur.next
            
        cur = self.head
        
        while cur is not None:
            cur.data = stack.pop()
            cur = cur.next
            
    def rev_without_list(self):
        cur = self.head
        prev = None
        
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
            
        
                       
        
l = LL()
l.insert_head(40)
l.insert_head(30)
l.insert_head(20)
l.insert_head(10)
# l.insert_end(50)
# l.insert_middle(80, 3)
# l.last_delete()
# l.sorted_insert(45)
# l.rev_list()
l.rev_without_list()
l.print_value()
