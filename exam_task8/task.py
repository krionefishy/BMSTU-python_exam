with open("exam_task8/ex.txt", "r", encoding="utf-8") as f:
    mx = 0
    
    string_list = []
    s = f.readline().split()
    len_st = len(s)
    while s:
        
        current = 0
        
        for i in range(len(s)):
            if current == 0:
                if s[i] == "#":
                    current += 1
                    
            else:
                if s[i] == "#" and s[i-1] == "#":
                    current += 1 
                else:
                    if mx < current:
                        flag = True
                        mx = current 
                    current = 0
        if current > mx:
            string_list = s
            mx = current
        
            
        s = f.readline().split()
        
    

    indexes = [i for i in range(len(string_list)) if string_list[i] == "#"]

    extra_string = [[0, i] for i in range(len_st)]
    
    f.seek(0)
    s = f.readline().split()
    while s:
        for i in indexes:
            if s[i] == "#":
                extra_string[i][0] += 1
        s = f.readline().split()
        
    
    sorted_sp = sorted(extra_string, key = lambda x: x[0], reverse = True)
    
with open("exam_task8/ex.txt", "r", encoding="utf-8") as f, open("exam_task8/o.txt", "w", encoding="utf-8") as o:
    s1 = f.readline().split()
    while s1:
        temp = []
        for i in sorted_sp:
            temp.append(s1[i[1]])
        o.write(" ".join(temp) + "\n")
        s1 = f.readline().split()
    o.write(" ". join([str(i[0]) for i in sorted_sp]))