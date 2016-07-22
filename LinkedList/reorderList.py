class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
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
        return prev

    def reorderList(self, head):
        if head==None or head.next==None:
            return head
        headtemp=ListNode(0)
        headtemp.next=head
        slow_ptr=head
        fast_ptr=head
        prev_to_slow=headtemp
        while fast_ptr!=None and fast_ptr.next!=None:
            fast_ptr=fast_ptr.next.next
            prev_to_slow=slow_ptr
            slow_ptr=slow_ptr.next
        prev_to_slow.next=None
        slow_ptr=Solution.reverseList(self,slow_ptr)
        curr1=headtemp.next
        curr2=slow_ptr
        while curr1!=None and curr2!=None:
            temp1=curr1.next
            temp2=curr2.next
            curr1.next=curr2
            curr2.next=temp1
            curr1=temp1
            curr2=temp2
        #print curr1,curr2
        temp3=headtemp.next
        while temp3.next!=None:
            temp3=temp3.next
        if curr1==None:
            temp3.next=curr2
        elif curr2==None:
            temp3.next=curr1
        #return headtemp.next    
        #Solution.printList(self,head)
        #Solution.printList(self, slow_ptr)

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
l1.next.next.next.next=ListNode(5)
sol=Solution()
sol.reorderList(l1)
sol.printList(l1)
l2=ListNode(3)

            
        