# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        listA = []
        listB = []
        headNode = head
        while headNode:
            currentValue = headNode.val
            if currentValue < x:
                listA.append(currentValue)
            else:
                listB.append(currentValue)
            headNode = headNode.next

        if listA:
            newHead = ListNode(listA[0])
            listA.pop(0)
        elif listB:
            newHead = ListNode(listB[0])
            listB.pop(0)
        else:
            newHead = None

        currentHead = newHead
        for entry in listA:
            newNode = ListNode(entry)
            currentHead.next = newNode
            currentHead = newNode
        for entry in listB:
            newNode = ListNode(entry)
            currentHead.next = newNode
            currentHead = newNode

        return newHead
