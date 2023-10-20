class node:
    
    def __init__(self, value):
        self.data = value
        self.next = None
        
def find_index(head, target):
    cur = head
    pos = 0
    
    if head == None:
        print("empty LL")
    
    while cur != None:
        if cur.data == target:
            print("the index is :-", pos)
            return
        cur = cur.next
        pos += 1
    
    if cur == None:
        print("item not found")
        
head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
find_index(head, 50)
