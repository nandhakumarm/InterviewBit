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
    def removeNthFromEnd(self, head, n):
        headtemp=ListNode(0)
        headtemp.next=head
        fast_ptr=headtemp
        slow_ptr=headtemp
        Solution.printList(self, headtemp)
        for i in range(n):
            if fast_ptr.next==None:
                return head.next
            fast_ptr=fast_ptr.next
        while fast_ptr.next!=None:
            fast_ptr=fast_ptr.next
            slow_ptr=slow_ptr.next
        slow_ptr.next=slow_ptr.next.next
        return headtemp.next
l1=ListNode(1)
l1.next=ListNode(4)
l1.next.next=ListNode(8)
l1.next.next.next=ListNode(12)
l1.next.next.next.next=ListNode(13)
sol=Solution()
sol.printList(sol.removeNthFromEnd(l1,7))
        