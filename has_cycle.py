def has_cycle(head):
    achados = []
    while head.next is not None:
        if head.next in achados:
            return 1
        achados.append(head.next)
        head = head.next
    return 0
