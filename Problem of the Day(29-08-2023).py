#Delete nodes having greater value on right
class Solution:
    def compute(self,head):
        curr=head
        prev=None
        nextt=None
        
        while(curr is not None):
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        
        
        head=prev
        
        
        current=head
        maxNode=head
        temp=None
        while(current is not None and current.next is not None):
            if current.next.data<maxNode.data:
                temp=current.next
                current.next=temp.next
            else:
                current=current.next
                maxNode=current
        curr=head
        prev=None
        
        while(curr is not None):
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        head=prev
        return head
