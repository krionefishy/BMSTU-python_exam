with open("exam_task9/in.txt", "r", encoding="utf-8") as f, open("exam_task9/out.txt", "w", encoding="utf-8") as o:
    ALPH = "qwertyuiopasdfghjklzxcvbnm"
    chars_to_delete = []
    s1 = list(f.readline())
    len_of_st = len(s1)
    for i in range(len(s1)):
        if s1[i] == "#":
            chars_to_delete.append(i)

    s1 = list(f.readline())
    while s1:
        for i in chars_to_delete:
            if s1[i] != "#":
                chars_to_delete.remove(i)
        s1 = list(f.readline())
    
    f.seek(0)
    s1 = list(f.readline())
    while s1:
        for i in chars_to_delete[::-1]:
            s1.pop(i)
        
        temp = "".join(s1).rstrip()
        c = 0
        
        for i in temp:
            if i.lower() in ALPH:
                c += 1
                
        temp += "."*(len_of_st - len(temp) - len(chars_to_delete)) + str(c)
        o.write(temp + "\n")
        s1 = list(f.readline())
        