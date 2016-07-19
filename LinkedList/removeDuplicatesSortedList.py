# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
    def deleteDuplicates(self, head):
        #if head==None:
            
        temp=head
        while temp!=None and temp.next!=None:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(2)
l1.next.next.next=ListNode(3)
l1.next.next.next.next=ListNode(3)
sol=Solution()
sol.printList(sol.deleteDuplicates(l1))
