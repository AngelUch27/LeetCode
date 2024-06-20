#https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        vl1 = []
        vl2 = []
        while current is not None:
            vl1.append(current.val)
            current = current.next  #Avanzando al siguiente nodo
        vl1.reverse()

        current = l2
        while current is not None:
            vl2.append(current.val)
            current = current.next  #Avanzando al siguiente nodo
        vl2.reverse()

        num1 = int(''.join(map(str, vl1)))
        num2 = int(''.join(map(str, vl2)))

        

        res = num1 + num2


        #Convertir el resultado en una lista enlazada invertida
        result_str = str(res)
        dummy = ListNode()
        current = dummy
        for char in result_str[::-1]:
            current.next = ListNode(int(char))
            current = current.next
        
        return dummy.next
