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
        
    def __str__(self):
        
        cur = self.head
        result = ""
        
        while cur != None:
            result += str(cur.data)+ "->"
            cur = cur.next
        return result[:-2]
    
    def append(self, value):
        
        new_node = node(value)
        
        if self.head ==  None:
            self.head = new_node
            self.n += 1
            return

        cur = self.head
        
        while cur.next != None:
            cur = cur.next

        cur.next = new_node
        self.n += 1
        
        
    def insert_after(self, after, value):
        
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
            print("not found")
            return
        
    def clear(self):
        self.head = None
        self.n = 0
        
    def del_head(self):
        if self.head == None: # the ll is empty
            print("empty ll")
            return
        
        self.head = self.head.next
        self.n -= 1
        
    def tail(self):
        cur = self.head

        if self.head == None: #if the ll is empty
            print("empty ll")
            return
        
        if cur.next == None: # if only one element in ll then just delete the head of the ll
            return self.del_head()
        
        while cur.next.next != None: # traverse till reach the second last element in the ll and then del the last element
            cur = cur.next
            
        cur.next = None #del the last element
        self.n -= 1
    
    def del_by_value(self, value):
        
        if self.head == None: # if the ll is empty
            print("empty ll")
            return 
        
        if self.head.data == value: # if we find the value at the head of the ll then delete head
            return self.del_head()
        
        cur = self.head 
        
        while cur.next != None: # we go till we find that the next item is the value we stop one element before the value
            if cur.next.data == value:
                break #if found then break
            cur = cur.next
            
        if cur.next != None: # if found then skip the value like next ko next.next kardo
            cur.next = cur.next.next
        else:
            print("not found") # else reached till last element but the element not found
            return
        
    def search(self, value):
        
        cur = self.head
        pos = 0
        
        while cur != None:
            if cur.data == value:
                return pos
            cur = cur.next
            pos += 1
        return "not found"
    
    def __getitem__(self, index): 
        cur = self.head
        pos = 0
        
        while cur != None:
            if pos == index:
                return cur.data
            
            cur = cur.next
            pos += 1
            
        return 'indexerror'
        
        
        
         

        
            
        
        
p = ll() 
print(p)
p.append(10)
p.append(20)
p.append(30)
p.insert_after(20,200)
print(p)
p.clear()
print(p)


        