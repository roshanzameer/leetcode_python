# Definition for singly-linked list.

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
        
class Solution:
    """
    1 >> 2 >> 4
    1 >> 3 >> 4
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next

if __name__ == '__main__':
    import sys
    from os.path import join, abspath, dirname
    dir_path = join(dirname(dirname(__file__)), 'data_structure')
    sys.path.insert(0, dir_path)
    from linked_list import LinkedList

    l1 = LinkedList()
    l1.insert_values([1,2,4])
    l1.print()

    l2 = LinkedList()
    l2.insert_values([1,3,4])
    l2.print()

    obj = Solution()
    tail = obj.mergeTwoLists(l1.head, l2.head)
    itr = tail
    while itr:
        print(itr.data)
        itr = itr.next