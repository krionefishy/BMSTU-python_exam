def shaker_sort(lst):
    left = 0
    right = len(lst) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(left,right):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
                is_sorted = False

        right -= 1
        
        for i in range(right, left - 1, -1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False 
        left += 1
    
    return lst 
