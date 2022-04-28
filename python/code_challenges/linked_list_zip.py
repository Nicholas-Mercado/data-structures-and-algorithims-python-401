from data_structures.linked_list import LinkedList

def zip_lists(a, b):



    a_current = a.head
    b_current = b.head

    while a_current and b_current:

        # temp holders
        a_temp_next = a_current.next
        b_temp_next = b_current.next

        # swap pointers
        a_current.next = b_current
        b_current.next = a_temp_next

        # iterate
        a_current =  b_current.next
        b_current =  b_temp_next
