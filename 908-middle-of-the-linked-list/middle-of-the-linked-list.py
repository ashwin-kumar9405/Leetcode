# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =head
        count =0
        while temp !=None:
            count +=1
            temp = temp.next
        pos =count//2
        temps = head
        for i in range(pos):
            temps = temps.next
        return temps