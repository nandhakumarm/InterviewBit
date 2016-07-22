class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution(object):
    def printList(self,A):
        temp=A
        while temp!=None:
            print temp.val,
            temp=temp.next
        print "done"
    
    def swapPairs(self, head):
        headtemp=ListNode(0)
        headtemp.next=head
        if head==None or head.next==None:
            return head
        curr=head
        next_to_curr=curr.next
        prev_to_curr=headtemp
        #Solution.printList(self, next_to_curr)
        head=next_to_curr
        while curr!=None and curr.next!=None:
            curr=prev_to_curr.next
            prev_to_curr.next=None
            next_to_curr=curr.next
            temp=curr.next.next
            next_to_curr.next=None
            next_to_curr.next=curr
            curr.next=temp
            prev_to_curr.next=next_to_curr
            prev_to_curr=curr
            curr=temp
            #next_to_curr=curr.next
            
        return head


l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
#l1.next.next.next.next=ListNode(5)
sol=Solution()
sol.printList(sol.swapPairs(l1))
l2=ListNode(3)
sol.printList(sol.swapPairs(l2))