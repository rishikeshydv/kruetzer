class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.nth = 0
class K_linkedlist():
    def __init__(self):
        self.ll = None
        self.head = self.tail =  None
        
    def lladd(self,val):
        if not val:
            raise ValueError("Node not fed")
        else:
            newNode = Node(val,None,1)
            if not self.head and not self.tail:
                self.head = newNode
                self.tail = newNode
                self.ll = newNode
            else:
                newNode.nth += self.ll.nth
                self.ll.next = newNode
                self.ll = self.ll.next
                self.tail = self.ll
                
    def lldel(self,nodeNum):
        if not nodeNum:
            raise ValueError("Dont know which node to delete")
        pre = self.pre(nodeNum)
        succ = self.post(nodeNum)
        pre.next = succ
        
        while succ:
            succ.nth -= 1
            succ = succ.next
            
    def llhead(self,val):
        if not val:
            raise ValueError("Node not fed. ")
        else:
            print(f"({self.head.val})", end=" -> ")
         
    def lltail(self,val):
        if not val:
            raise ValueError("Node not fed. ")
        else:
            print(f"({self.tail.val})", end=" -> ")
        
    
    def pre(self,val):
        p = None
        if not val:
            raise ValueError("Dont know what node to find precedessor for.")
        if not self.ll:
            raise ValueError("No Linked List Created.")
        
        if self.head.nth == val:
                return
            
        while self.ll:
            if not self.ll.nth == val:
                p = self.ll
                self.ll = self.ll.next
            
        if p:
            return p
        else:
            raise ValueError("No such node found")
        
    
    def post(self,val):
        q = Node(None)
        if not val:
            raise ValueError("Dont know what node to find successor for.")
        if not self.ll:
            raise ValueError("No Linked List Created.")
        
        if self.head.nth == val:
                return
            
        while self.ll:
            if self.ll.nth != val:
                self.ll = self.ll.next
            else:
                q = self.ll.next   
            
        if q:
            return q
        else:
            raise ValueError("No such node found")
                  
    
    def displayll(self):
        if not self.ll:
            raise ValueError("Empty Linked List")
        while self.ll:
            print(f"({self.ll.val})", end=" -> ")
            self.ll = self.ll.next
            print("None")
        
    