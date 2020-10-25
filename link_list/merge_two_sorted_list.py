# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

# Approach: Using only 1 while loop
# create a new listNode head and assign 0 as value and make a pointer points to it.
# start iterating, we will be checking if list1 value is less the list2 value and vice versa, whichever condition satisfies make the 
# value as smaller value and create a new node with smaller value and now pointer next points to new node, and move pointer to new node
# after all these operation, remember we have head pointing to first node which is 0, so we will be returning head.next nodes.

# handling cases if length of both list are different:
# if list1 value is none then we know that both list are sorted so we can just append pointer next node to list2 nodes and vice versa

# space:O(m+n) = O(n)
# time:O(m+n) = O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                ptr.next = l2
                break
            if l2 is None:
                ptr.next = l1
                break
            smaller_val = 0
            if l1.val < l2.val:
                smaller_val = l1.val
                l1 = l1.next
            else:
                smaller_val = l2.val
                l2 = l2.next
            new_node = ListNode(smaller_val)
            ptr.next = new_node
            ptr = ptr.next
        return head.next