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
    
    def rotateRight(self, head, k):
        if head==None:
            return head
        tempoList=head
        length=0
        while tempoList!=None:
            length+=1
            tempoList=tempoList.next
        print length
        if k>length:
            k=k%length
        if k==0:
            return head
        headtemp=ListNode(0)
        headtemp.next=head
        fast_ptr=headtemp
        slow_ptr=headtemp
        #Solution.printList(self, headtemp)
        for i in range(k):
            if fast_ptr.next==None:
                return head.next
            fast_ptr=fast_ptr.next
        while fast_ptr.next!=None:
            fast_ptr=fast_ptr.next
            slow_ptr=slow_ptr.next
        temp=slow_ptr.next
        slow_ptr.next=None
        temp2=temp
        while temp2.next!=None:
            temp2=temp2.next
        temp2.next=headtemp.next
        return temp
        #Solution.printList(self, headtemp)
        #Solution.printList(self, temp)

l1=ListNode(1)
l1.next=ListNode(4)
l1.next.next=ListNode(8)
l1.next.next.next=ListNode(12)
l1.next.next.next.next=ListNode(13)

l2=ListNode(2)
sol=Solution()
sol.printList(sol.rotateRight(l1,10))