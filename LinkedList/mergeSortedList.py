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
    
    def mergeTwoLists(self, l1, l2):
        head=ListNode(0)
        headtemp=head
        if l1==None:
            return l2
        if l2==None:
            return l1
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp=l1.next
                headtemp.next=l1
                headtemp.next.next=None
                l1=temp
                headtemp=headtemp.next
            else:
                temp=l2.next
                headtemp.next=l2
                headtemp.next.next=None
                l2=temp
                headtemp=headtemp.next
        if l1==None:
            #while l2!=None:
            headtemp.next=l2
        elif l2==None:
            headtemp.next=l1       
        #Solution.printList(self, head.next)
        return head.next


l1=ListNode(1)
l1.next=ListNode(4)
l1.next.next=ListNode(8)
l1.next.next.next=ListNode(12)
l1.next.next.next.next=ListNode(13)

l2=ListNode(2)
l2.next=ListNode(3)
l2.next.next=ListNode(7)
#l1.next.next.next=ListNode(2)
#l1.next.next.next.next=ListNode(3)
sol=Solution()
sol.printList(sol.mergeTwoLists(l1, l2))