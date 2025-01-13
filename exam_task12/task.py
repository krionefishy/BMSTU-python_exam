with open("exam_task12/in.txt", "r", encoding="utf-8") as f, open("exam_task12/out.txt", "w", encoding="utf-8") as o:
    co = {}
    s = f.readline()
    while s:
        s = s.replace(">", " ")
        s = s.replace("<", " ")
        s = s.split()
        
        current = 1
        is_open = False 
        for i in s:
            if "/" not in i:
                is_open = True 
                if i in co:
                    co[i][0] += 1
                    co[i][1] = max(co[i][1], current)
                else:
                    co[i] = [0,0]
                    co[i][0] = 1
                    co[i][1] = current
                current += 1
            else:
                current -= 1
        s = f.readline()
        
        
    l = sorted(co, reverse = True)
    for i in l:
        s = i + " " + str(co[i][0]) + " " + str(co[i][1])
        o.write(s + "\n")