'''

with open("task1/in.txt", "r", encoding="utf-8") as input_file, open("task1/out.txt", 'a', encoding="utf-8") as out_file:
    current_string = ""
    part_of_string = ""
    s = input_file.readline()
    while s:
        parts = s.split(".")
        parts = [i for i in parts if len(i) > 0]
        
                
        if part_of_string:
            out_file.seek(0,0)
            out_file.write(part_of_string + parts.pop(0) + '.' + "\n")
            part_of_string = ''
        else:
            for i in range(len(parts) - 1):
                out_file.seek(0,0)
                out_file.write(parts[i] + '.' + '\n')
            if s[-1] == '.':
                out_file.seek(0,0)
                out_file.write(parts[-1] + '.' + '\n')
            else:
                part_of_string = parts[-1]
                    
                    
        s = input_file.readline()

'''

cur = "a"
'''last_line = ''
with open("task1/out.txt", "a+") as file:

    file.seek(0, 2)  
    position = file.tell()  
    while position:  
        file.seek(position - 1)  
        char = file.read(1) 
        if char == '\n' and position != 1:  
            break  
        last_line = char + last_line  
        position -= 1  
    file.write(f"\n{last_line}")
    '''
    
"""with open("task1/out.txt", "w") as f:
    f.seek(0,0)
    f.write("a")"""
'''if len(part_of_string) != 0:
            if len(parts) == 1:
                if '.' in s:
                    out_file.seek(0,0)
                    out_file.write(part_of_string + parts[0] + '.' + '\n')
                else:
                    part_of_string += s
            else:
                if s.count(".") == 2:
                    out_file.seek(0,0)
                    out_file.write(part_of_string+parts[0] + '.' + '\n')
                    out_file.seek(0,0)
                    out_file.write(parts[1] + '.' + '\n')
                elif s.count(".") == 1:
                    out_file.seek(0,0)
                    out_file.write(part_of_string+parts[0] + '.' + '\n')
                    part_of_string = parts[1]
                else:'''
                
'''with open("task1/in.txt", "r", encoding="utf-8") as input_file, open("task1/out.txt", 'a', encoding = 'utf-8') as out_file:
    input_file.seek(0,2)
    pos = input_file.tell()
     
    string = ''
    for k in range(pos-2,-1,-1):
        input_file.seek(k)
        char = input_file.read(1)
        if char == "\n":
            continue
        if char == ".":
            out_file.write(f"{string[::-1].strip().strip('.')}.\n")
            string = ''
        else:
            string += char 
    
    out_file.write(f"{string[::-1].strip().strip('.')}.\n")'''
    
    
    
'''with open("task1/in.txt", "r", encoding="utf-8") as input_file, open("task1/out.txt", 'a', encoding='utf-8') as out_file:
    input_file.seek(0,2)
    pos = input_file.tell()
     
    string = ''
    for k in range(pos-2,-1,-1):
        input_file.seek(k)
        char = input_file.read(1)
        if char == "\n":
            continue
        if char == ".":
            out_file.write(f"{string[::-1].strip().strip('.')}.\n")
            string = ''
        else:
            string += char 
    if len(string.strip().strip(".")) > 1:
        out_file.write(f"{string[::-1].strip().strip('.')}.\n")'''

import os
        
        
with open("two_texts/in.txt", "r", encoding="utf-8") as input_file, open("two_texts/temp.txt", 'w', encoding = 'utf-8') as out_file:
    char = input_file.read(1)
    s_count = 0
    sentence = ""
    while char:
        if char != "\n":
            sentence+=char
            if char == '.':
                out_file.write(f"{sentence.strip()}\n")
                s_count += 1
                sentence = ""
        char = input_file.read(1)
    
    
    
with open("two_texts/temp.txt", "r", encoding="utf-8") as t, open("two_texts/out.txt", "w", encoding="utf-8") as o:
    k = s_count
    for i in range(k):
        co = 1
        while co <= s_count:
            string = t.readline()
            co += 1
        o.write(string)
        t.seek(0)
        s_count -= 1
        
os.remove("two_texts/temp.txt")