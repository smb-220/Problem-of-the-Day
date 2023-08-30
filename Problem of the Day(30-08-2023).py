#Delete a Node in Single Linked List
def delNode(head, k):
    if k == 1:
        return head.next
    temp = head
    cnt = 1
    temp2 = head
    while k != cnt and temp is not None:
        temp2 = temp
        temp = temp.next
        cnt+=1
    
    temp2.next = temp.next
    del temp
    return head
