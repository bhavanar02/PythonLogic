class Solution:
    def deleteDuplicates(head):
        if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
    
    print(deleteDuplicates({1, 2, 3, 3, 4, 5}))