with open("exam_task10/in.txt", "r", encoding="utf-8") as f, \
    open("exam_task10/temp.txt", "w+", encoding="utf-8") as t, \
    open("exam_task10/out.txt", "w", encoding = "utf-8") as o:
    s = f.readline()
    num = 0
    ctr = []
    while s:
        mx_len = len(max(s.split(), key = len))
        current = [i + (mx_len - len(i))*" " for i in s.split()]
        
        for i in range(mx_len):
            num += 1
            temp = ""
            co = 0
            for j in current:
                temp += j[i]
                if j[i].isalpha():
                    co += 1
            t.write(temp + "\n")
            ctr.append((co, num))
        s = f.readline()
        
    
        
    sorted_ctr = sorted(ctr, key = lambda x: x[0])
    
    t.seek(0)
    for i in sorted_ctr:
        n = 1
        s = t.readline()
        while n != i[1]:
            s = t.readline()
            n += 1
        o.write(s)
        t.seek(0)