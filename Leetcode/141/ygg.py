# cannot be executed in local
def hasCycle(self, head: Optional[listNode]) -> bool:
    # head.next 체크 깜빡함
    if head == None or head.next == None:
        return False
    first = head
    second = head.next

    # idea: if two pointer (1 jump, 2 jump) meets each other
    while second != None:
        if first == second:
            return True
        first = first.next
        if second.next == None:
            return False
        else:
            second = second.next.next
    return False