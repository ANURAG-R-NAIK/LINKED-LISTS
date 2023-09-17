class node:
    
    def __init__(self, value):
        self.data = value # pass the value of the ll
        self.next = None # every node created has next as None
        
n1 = node(10)
n2 = node(20)
n3 = node(30)
head = n1
n1.next = n2
n2.next = n3

print(n3.next)