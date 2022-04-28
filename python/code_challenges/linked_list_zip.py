from data_structures.linked_list import LinkedList

def zip_lists(a, b):


    a_current = a.head
    b_current = b.head

    if 

    while a_current and b_current:

        # temp holders
        a_temp_next = a_current.next
        b_temp_next = b_current.next

        print('b_current',b_current)
        print('a_current',a_current)
        # swap pointers
        if not a_current.next:
            a_current.next = b_current
            break

        a_current.next = b_current
        b_current.next = a_temp_next


        # iterate
        a_current =  b_current.next
        b_current =  b_temp_next

    return a

