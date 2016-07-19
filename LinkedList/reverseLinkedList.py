class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
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

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
l1.next.next.next.next=ListNode(5)
sol=Solution()
l2=sol.reverseList(l1.next.next)
#print l2.val,l2.next.val,l2.next.next.val
sol.printList(l2)
sol.printList(l1)