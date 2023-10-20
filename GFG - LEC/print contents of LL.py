class node:
    
    def __init__(self, value):
        self.data = value
        self.next = None
        
def print_values(head):
    cur = head
    
    while cur != None:
        print(cur.data, "->", end = "")
        cur = cur.next
        
head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
print_values(head)