# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getLength(self,A):
        length=0
        temp=A
        if temp==None:
            return 0
        if temp.next==None:
            return 1
        while temp!=None:
            length+=1
            temp=temp.next
        return length
    
    def getIntersectionNode(self, A, B):
        len1=Solution.getLength(self, A)
        len2=Solution.getLength(self, B)
        tempA=A
        tempB=B
        diffrence=0
        if len1>len2:
            diffrence=len1-len2
            for i in range(0,diffrence):
                tempA=tempA.next
            
        else:
            diffrence=len2-len1
            for i in range(0,diffrence):
                tempB=tempB.next
            
        while tempA!=None and tempB!=None:
            if tempA==tempB:
                return tempA
            tempA=tempA.next
            tempB=tempB.next
        return None
            
