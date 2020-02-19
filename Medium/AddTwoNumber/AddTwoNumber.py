# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self, node):
        self.head = node
        self.tail = node

    def append(self, L: list):
        while len(L) != 0:
            v = L.pop(0)
            self.tail.next = ListNode(v)
            self.tail = self.tail.next

    def printNode(self):
        a = self.head
        print(a.val, end=' ')
        while a.next != None:
            a = a.next
            print(a.val, end=' ')
        print()


class Solution:
    def __init__(self):
        self.answer = []

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # python中餐數列會用:當作註解 表示傳進來是甚麼type ->則代表function回傳的是甚麼type
        if l1 == None:

            return l2
        if l2 == None:

            return l1
        ansNode = ListNode(0)
        if (l1.val + l2.val) < 10:

            ansNode.val = l1.val+l2.val
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)

            return ansNode
        elif (l1.val + l2.val) >= 10:
            ansNode.val = l1.val+l2.val-10
            ansNode.next = self.addTwoNumbers(
                ListNode(1), self.addTwoNumbers(l1.next, l2.next))

            return ansNode


l1 = ListNode(2)
l2 = ListNode(5)
LIST = List(l1)
LIST2 = List(l2)
array = [4, 3]
array2 = [6, 4]
LIST.append(array)
LIST2.append(array2)
LIST.printNode()
LIST2.printNode()
ANS = Solution()
ANS.addTwoNumbers(l1, l2)
