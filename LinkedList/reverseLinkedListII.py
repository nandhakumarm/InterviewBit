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
    def reverseBetween(self, head, m, n):
        #Solution.printList(self, head)
        headtemp=ListNode(0)
        headtemp.next=head
        start=head
        end=head
        prev_to_start=headtemp
        next_to_end=end.next
        ctr=1
        while ctr<m:
            prev_to_start=start
            start=start.next
            end=end.next
            next_to_end=end.next
            ctr+=1
        
        prev_to_start.next=None
        while ctr<n:
            end=end.next
            next_to_end=end.next
            ctr+=1
        end.next=None
        revList=Solution.reverseList(self, start)
        temp=revList
        while temp.next!=None:
            temp=temp.next
        temp.next=next_to_end
        prev_to_start.next=revList
        return headtemp.next
        Solution.printList(self, head)
        Solution.printList(self, prev_to_start)
        Solution.printList(self, start)
        Solution.printList(self, end)
        Solution.printList(self, next_to_end)
        Solution.printList(self, revList)
        Solution.printList(self, headtemp.next)
        print prev_to_start==None
        print next_to_end==None
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l1.next.next.next=ListNode(4)
l1.next.next.next.next=ListNode(5)
sol=Solution()
sol.printList(sol.reverseBetween(l1, 4, 5))
l2=ListNode(2)
sol.printList(sol.reverseBetween(l2, 1, 1))
                    