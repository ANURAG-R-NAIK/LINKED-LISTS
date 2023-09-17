class node:
    
    def __init__(self, value):
        self.data = value #we will pass the value here
        self.next = None # we will keep default adress as none when creating a node
        
        
class ll:
    
    def __init__(self): # here we are creating an empty linked list
        
        self.head = None
        self.n = 0 # keeps count of the number of nodes 
        
    def __len__(self): # len of linked list is the number of nodes 
        return self.n
    
    def insert_at_head(self, value):
        
        # create node
        new_node = node(value)
        
        #create connection
        new_node.next = self.head
        
        #reassign head
        self.head = new_node
        
        #increment n
        self.n += 1
        
    def traverse(self):
        
        cur = self.head
        
        while cur != None:
            
            print(cur.data)
            cur = cur.next
        
    def apppend(self, value):
        
        new_node = node(value)
        
        if self.head == None: #if wmpty ll then we make the new node itself as head
            # empty LL
            self.head = new_node
            self.n += 1
            return 
        
        cur = self.head
        
        while cur.next != None:
            
            cur = cur.next
            
        #now at this point u are at the last node  
        cur.next = new_node  # this appending works when ll is not empty
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
            return 'item not found'
        # case 1 break -> after is found
        # case 2 -> item is not found -> cur -> None
            
        print(cur.data)
            
            
        
        
        
l = ll()
l.insert_at_head(1)
l.insert_at_head(2)
l.insert_at_head(3)
l.insert_at_head(4)

l.insert_after(20, 200)

print(l.traverse())

# print("-----------")
# l.apppend(5)
# print(len(l))
# print(l.traverse())


