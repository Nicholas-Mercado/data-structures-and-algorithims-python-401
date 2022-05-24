

def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[0:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, lst)

def merge(left, right, lst):
    pass
