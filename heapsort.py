
def left(i):
    return 2*i + 1

def right(i):
    return 2 * i + 2

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    
def heaplify(lst, i, n):
    left_el = left(i)
    right_el = right(i)
    
    largest = i
    
    if left_el < n and lst[left_el] > lst[largest]:
        largest = left_el 
    if right_el < n and lst[right_el] > lst[largest]:
        largest = right_el
    
    if largest != i:
        swap(lst, largest, i)
        heaplify(lst, largest, n)
        
        
def pop(lst, n):
    if n <= 0:
        return 
    
    swap(lst, 0, n-1)
    heaplify(lst, 0, n-1)
    
    
def heap_sort(lst):
    if len(lst) <= 1:
        return lst 
    
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heaplify(lst, i, n)
        
        
    for i in range(n - 1, 0, -1):
        pop(lst, i + 1)
        
    return lst


