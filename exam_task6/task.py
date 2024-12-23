def float_to_oct(s):
    left_part = oct(int(s))[2:]
    
    right_part = s - int(s)
    
    dropnaya = []
    while right_part:
        right_part *= 8
        dropnaya.append(str(int(right_part)))
        right_part -= int(right_part) 
        if len(dropnaya) > 4:
            break
        
    return left_part + "." + "".join(dropnaya)


def replace_numbers(string):
    ch = ""
    nums_to_replace = []
    for i in range(len(string)):
        if string[i] in "0123456789":
            ch += string[i]
        elif string[i] in "abcdefABCDEFx":
            ch += string[i]
        elif string[i] == "." and "." not in ch:
            ch += string[i]
        else:
            if len(ch) > 0:
                if not ch.startswith("0x"):
                    ch = "0x" + ch
                num = float_to_oct(float.fromhex(ch))
                nums_to_replace.append((ch, num))
                ch = ""
                
    for i in nums_to_replace:
        string = string.replace(i[0],i[1],1)
    
    return string


with open("exam_task6/in.txt", "r", encoding="utf-8") as input_file, open("exam_task6/out.txt", 'w', encoding = 'utf-8') as out_file:
    char = input_file.read(1)
    sentence = ""
    is_number = False 
    not_tochechka = True
    while char:
        if char in "0123456789abcdfABCDEFx":
            is_number = True 
            
        if char != "\n":
            sentence+=char
            if char == '.':
                if is_number and not not_tochechka: 
                    out_file.write(f"{replace_numbers(sentence.strip())}\n")
                    sentence = ""
                    is_number = False 
                    not_tochechka = True
                elif not is_number:
                    out_file.write(f"{replace_numbers(sentence.strip())}\n")
                    sentence = ""
                    not_tochechka = True
                
                elif is_number and not_tochechka:
                    not_tochechka = False 
    
        char = input_file.read(1)