# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        beforeNode = None
        currentSumNode = None
        upperValue = 0
        head = None
        while l1 or l2:
            if currentSumNode:
                beforeNode = currentSumNode

            if l1 and l2:
                currentSum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                currentSum = l1.val
                l1 = l1.next
            elif l2:
                currentSum = l2.val
                l2 = l2.next
            currentSumNode = ListNode((currentSum + upperValue) % 10)
            if beforeNode == None:
                head = currentSumNode
            else:
                beforeNode.next = currentSumNode
            upperValue = (currentSum + upperValue) // 10
        if upperValue:
            currentSumNode.next = ListNode(upperValue)
        return head


