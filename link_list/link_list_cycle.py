# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, 
# pos is used to denote the index of the node that tail's next pointer is connected to

# Solution 1:  two pointer approach, space : O(1), time : O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow_ptr = head
        fast_ptr = head.next.next
        while slow_ptr is not None and  fast_ptr is not None and fast_ptr.next is not None:
            if slow_ptr == fast_ptr:
                return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return False

# Solution 2: Changing the nodes value of the ones I visited already, space : O(1), time : O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        while head:
            if head.val == "a":
                return True
            else:
                head.val = "a"
            head = head.next
        return false