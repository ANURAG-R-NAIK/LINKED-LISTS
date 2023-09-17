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
        
    def __str__(self): # travesring the ll here we have taken __str__ just to print the value 
        
        cur = self.head # present cur will be first initialised to the head of the ll
        
        result = ""
        while cur != None: # whenever we eant to traverse till the last element we give this 
            result += str(cur.data) + "->"
            cur = cur.next
        return result[:-2]
        
        
        
l = ll()
l.insert_at_head(1)
l.insert_at_head(2)
l.insert_at_head(3)
l.insert_at_head(4)
# print(len(l))
print(l)