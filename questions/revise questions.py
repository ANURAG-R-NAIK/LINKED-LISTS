# def maximum(l, value):
    
#     cur = self.head
#     maxi = cur
    
#     while cur != None:
#         if cur.data > maxi:
#             maxi = cur
            
            
#         cur = cur.next
    
#     max.data = value


def sum_odd(self):
    
    cur = self.head
    summ = 0
    index = 0
    
    
    while cur != None:
        if index % 2 != 0:
            summ += cur.data
        cur = cur.next
        index += 1
    return summ        
        