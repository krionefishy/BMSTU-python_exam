def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j + 1], lst[j]
    return lst 

def bubble_sort_with_flag(lst):
    n = len(lst)
    for i in range(n):
        swapped = False 
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True 
                lst[j], lst[j+1] = lst[j+1], lst[j] 
        if not swapped:
            break
    return lst

