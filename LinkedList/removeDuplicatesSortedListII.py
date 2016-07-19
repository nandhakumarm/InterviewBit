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
        temp1=ListNode(0)
        temp1.next=head
        temp2=temp1
        while temp2.next!=None and temp2.next.next!=None:
            if temp2.next.val== temp2.next.next.val:
                item=temp2.next.val
                while temp2.next!=None and temp2.next.val==item:
                    temp2.next=temp2.next.next
            else:
                temp2=temp2.next
        return temp1.next

l1=ListNode(1)
l1.next=ListNode(1)
l1.next.next=ListNode(2)
l1.next.next.next=ListNode(2)
l1.next.next.next.next=ListNode(3)
#l1.next.next.next.next.next=ListNode(3)
#l1.next.next.next.next.next.next=ListNode(4)
sol=Solution()
sol.printList(sol.deleteDuplicates(l1))
