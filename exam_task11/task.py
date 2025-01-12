def calc(lst):
    match lst[1]:
        case "+":
            return int(lst[0]) + int(lst[2])
        case "-":
            return int(lst[0]) - int(lst[2])
        case "*":
            return int(lst[0]) * int(lst[2])
        case "/":
            return int(lst[0]) / int(lst[2])


def find_longest_subarray(lst):
    res = []
    temp = [lst[0][0]]
    prev, prev_len = lst.pop(0)
    mx_len = prev_len
    while lst:
        current, cur_len = lst.pop(0)
        if current != prev + 1:
            temp.append(prev)
            res.append((temp, mx_len))
            temp = [current]
            mx_len = cur_len
        else:    
            mx_len = max(mx_len, cur_len)
            
        prev = current
    temp.append(prev)
    res.append((temp, mx_len))
    return max(res, key = lambda x: (x[0][1] - x[0][0]))

#print(find_longest_subarray([(1, 21), (2, 22), (4, 28), (5, 23), (6, 21)]))

def align_wigth(s, l):
    cur_l = len(s)
    if cur_l == l:
        return s
    co_of_sp = len(s.split()) - 1
    diff = l - cur_l
    if co_of_sp == 0:
        return " "*diff + s 
    if co_of_sp == 1:
        s = s.replace(" ", " "*(diff + 1))
        return s 
    
    res = (" "*(diff//co_of_sp + 1)).join(s.split())
    if diff % co_of_sp > 0:
        res = res.replace(" ", " " * (diff % co_of_sp + 1), 1) 
    return res 


with open("exam_task11/in.txt", "r", encoding="utf-8") as f, open("exam_task11/out.txt", "w", encoding="utf-8") as o:
    lst = []
    s = f.readline()
    n = 0
    while s:
        n += 1
        len_current = len(s)
        s = s.split()
        is_positive = False
        for i in range(len(s)):
            if s[i] in "+-*/":
                is_positive = calc(s[i-1:i+2]) > 0
                break
        if is_positive:
            lst.append((n, len_current))
        
        s = f.readline()    
            
    diap, est_len = find_longest_subarray(lst)
    del lst
    
    f.seek(0)
    s = f.readline().strip("\n")
    num = 0
    while num < diap[1]:
        
        num += 1
        if num >= diap[0]:
            
            res = align_wigth(s, est_len) + "\n"
            o.write(res)

        s = f.readline().strip("\n")