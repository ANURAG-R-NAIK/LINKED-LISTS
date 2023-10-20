class node:
    
    def __init__(self, value):
        self.data = value
        self.next = None
        
class LL:
    
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_head(self, new):
        new_node = node(new)
        
        new_node.next = self.head
        self.head = new_node
        
        self.n += 1
        
        
    def traverse(self):
        
        cur = self.head
        
        while cur != None:
            print(cur.data, '->', end = " ")
            
            cur = cur.next
            
    def __str__(self):
        
        cur = self.head
        
        res = ""
        
        while cur != None:
            res = res + str(cur.data) + "->"
            
            cur = cur.next
        return res[:-2]
        
    def tail_append(self, value):
        new_node = node(value)
        
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        cur = self.head
        
        while cur.next != None:
            cur = cur.next
            
        cur.next = new_node
        self.n += 1
        
    def middle_insert(self, after, value):
        
        new_node = node(value)
        
        cur = self.head
        while cur != None:
            if cur.data == after:
                break
            cur = cur.next
            
        if cur != None:
            new_node.next = cur.next
            cur.next = new_node
            self.n += 1
        else:
            print("item not found")
            
    def __clearll__(self):
        self.head = None
        self.n = 0
        
    def head_delete(self):
        
        if self.head == None:
            print("empty LL")
        else:
            self.head = self.head.next
            self.n -= 1   
            
    def delete_tail(self):
        cur = self.head
        
        if cur == None:
            print("empty LL")
            
        if cur.next == None:
            return self.head_delete()
        
        while cur.next.next != None:
            cur = cur.next
        
        cur.next = None
        self.n -= 1
        
    def del_by_value(self, value):        
        cur = self.head
        
        if cur == None:
            print("empty LL")
        
        if cur.data == value:
            return self.head_delete()
        
        while cur.next != None:
            if cur.next.data == value:
                break
            cur = cur.next
            
        if cur.next == None:
            print("not found")
        else:
            cur.next = cur.next.next
            
    def search(self, value):
        
        cur = self.head
        
        pos = 0
        
        while cur != None:
            if cur.data == value:
                print(pos)
                return
            cur = cur.next 
            pos += 1
        print("not found")
        
    def __getitem__(self, index):
        # __getitem__ is used to find the element based on the index given 
        cur = self.head
        
        pos = 0
        
        while cur != None:
            if pos == index:
                return cur.data
            cur = cur.next
            pos += 1
        
        
l = LL()
l.insert_head(5)
l.insert_head(4)
l.insert_head(3)
l.insert_head(2)
l.insert_head(1)
l.tail_append(10)
l.head_delete()
l.delete_tail()
# l.middle_insert(300, 30)
print(len(l))
# l.traverse()
# print()
print(l)
l.search(3)
print(l[0])
