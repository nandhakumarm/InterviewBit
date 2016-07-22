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
    def detectCycle(self, head):
        if head==None or head.next==None:
            return None
        slow_ptr=head
        fast_ptr=head
        while fast_ptr!=None and fast_ptr.next!=None:
            if slow_ptr==fast_ptr:
                slow_ptr=head
                while slow_ptr!=fast_ptr:
                    slow_ptr=slow_ptr.next
                    fast_ptr=fast_ptr.next
                return slow_ptr.val
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        return None