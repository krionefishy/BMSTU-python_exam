def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        
    return lst

def insertion_with_barrier(lst):
    barrier = 0
    n = len(lst)
    for i in range(1,n):
        barrier +=1 
        key = lst[i]
        j = barrier - 1
        
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def binary_search(lst, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == key:
            return mid + 1
        if lst[mid] < key:
            left = mid + 1
        elif lst[mid] > key:
            right = mid - 1
    return left 


def binary_insertion(lst):
    n = len(lst)
    for i in range(1,n):
        key = lst[i]
        pos = binary_insertion(lst, 0, i - 1, key)
        
        lst[pos+1: i + 1] = lst[pos:i]