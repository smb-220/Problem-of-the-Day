class Solution:
    def rearrange(self, head):
        odd = head
        if (odd is None or odd.next is None or odd.next.next is None):
            return
        even = odd.next
        
        odd.next = odd.next.next
        odd = odd.next
        even.next = None
        while (odd and odd.next):
            temp = odd.next.next
            odd.next.next = even
            even = odd.next
            odd.next = temp
            if temp is not None:
                odd = temp
        odd.next = even
