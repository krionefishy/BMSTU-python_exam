def shell_sort(lst):
    inc = len(lst) // 2
    n = len(lst)
    while inc > 0:
        for i in range(inc, n):
            temp = lst[i]
            j = i
            while j >= inc and lst[i - inc] > temp:
                lst[j] = lst[j - inc]
                j -= inc 
            lst[j] = temp
        
        inc //= 2
    return lst

