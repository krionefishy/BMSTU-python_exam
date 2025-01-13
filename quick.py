def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    return quicksort([i for i in lst if i < pivot]) + [ i for i in lst if i == pivot] + quicksort([i for i in lst if i > pivot])


