from data_structures.linked_list import LinkedList

def zip_lists(a, b):


    a_current = a.head
    b_current = b.head
    # conditional logic for empty a list
    if not a_current:
        return b
    # conditional logic for empty a list
    if not b_current:

        return a
    while a_current and b_current:

        # temp holders
        a_temp_next = a_current.next
        b_temp_next = b_current.next

        # conditional for short b list
        if not a_current.next:
            a_current.next = b_current
            break
        # swap pointers
        a_current.next = b_current
        b_current.next = a_temp_next


        # iterate
        a_current =  b_current.next
        b_current =  b_temp_next
    # conditional for a short because returning rest of a
    return a

