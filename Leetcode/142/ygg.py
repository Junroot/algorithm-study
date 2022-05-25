# cannot be executed in local
def hasCycle(self, head: Optional[listNode]) -> bool:
    # head.next 체크 깜빡함
    if head == None or head.next == None:
        return None
    first = head
    second = head.next

    # idea: when 2 pointers meet, cycle point length is same as the distance from meeting point to last point of the cycle
    while second != None:
        if first == second:
            start = head
            while start != first:
                start = start.next
                first = first.next
            return start
        first = first.next
        if second.next == None:
            return None
        else:
            second = second.next.next
    return None