def s(lst):
    n = len(lst)
    for i in range(n):
        mn = i
        for j in range(i+1, n):
            if lst[j] < lst[mn]:
                mn = j
                
        lst[i], lst[mn] = lst[mn], lst[i]
        
    return lst 


