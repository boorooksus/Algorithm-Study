class ListNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head

        self.k, self.len = k, 0

    def _add(self, node, new):
        new.left, new.right, node.right.left, node.right = node, node.right, new, new

    def _del(self, node):
        node.right.right.left, node.right = node, node.right.right

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False

        self.len += 1

        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False

        self.len += 1

        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False

        self.len -= 1

        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False

        self.len -= 1
        self._del(self.tail.left.left)

        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.right.val if self.len > 0 else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.left.val if self.len > 0 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()