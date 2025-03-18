# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head, prev_node, new_node = ListNode(0, None), None, ListNode(0, None)
        result = carry = 0

        while l1 or l2:
            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0
            result = op1 + op2 + carry
            
            if result > 9:
                carry = result // 10
                result %= 10
            else:
                carry = 0
            
            print(f"op1: {op1}, op2: {op2}, result: {result}, carry: {carry}")
            new_node = ListNode(result, None)
            
            if prev_node:
                prev_node.next = new_node
                prev_node = prev_node.next
            else:
                result_head = prev_node = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            new_node = ListNode(carry, None)
            prev_node.next = new_node
            prev_node = prev_node.next

        return result_head
