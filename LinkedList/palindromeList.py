class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printList(self,A):
        temp=A
        while temp!=None:
            print temp.val,
            temp=temp.next
        print "done"
    def reverseList(self, A):
        curr=A
        prev=None
        #temp=curr
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        print "in reverse"
        Solution.printList(self, prev)
        return prev
    
    def lPalin(self, head):
        if head==None or head.next==None:
            return 1
        
        # fast and slow pointer to find the mid of the node
        #midnode variable stores the middle element in case of odd number of nodes
        slow_ptr=head
        fast_ptr=head
        prev_to_slow=head
        midnode=None
        while fast_ptr!=None and fast_ptr.next!=None:
            fast_ptr=fast_ptr.next.next
            prev_to_slow=slow_ptr
            slow_ptr=slow_ptr.next
        if fast_ptr!=None:
            midnode=slow_ptr
            slow_ptr=slow_ptr.next
        prev_to_slow.next=None
        revHalf=Solution.reverseList(self, slow_ptr)
        ptrRevHalf=revHalf
        #Solution.printList(self, head)
        #Solution.printList(self, revHalf)
        temp=head
        while temp!=None:
            if temp.val!=revHalf.val:
                return 0
            temp=temp.next
            revHalf=revHalf.next
        revHalf=Solution.reverseList(self, ptrRevHalf)
        if midnode!=None:
            prev_to_slow.next=midnode
            prev_to_slow=prev_to_slow.next
        prev_to_slow.next=revHalf
        return 1
        
        #Solution.printList(self, head)
        #Solution.printList(self, revHalf)
        

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(2)
l1.next.next.next=ListNode(1)
#l1.next.next.next.next=ListNode(5)
sol=Solution()
sol.printList(l1)
print sol.lPalin(l1)
sol.printList(l1)
#l2=sol.reverseList(l1)
#print l2.val,l2.next.val,l2.next.next.val