class node:
    
    def __init__(self,value):
        self.data = value
        self.next = None
        
# temp1 = node(10)
# temp2 = node(20)
# temp3 = node(30)
# head = temp1
# temp1.next = temp2
# temp2.next = temp3

head = node(10)
head.next = node(20)
head.next.next = node(30)