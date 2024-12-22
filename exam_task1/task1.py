def count_palindromes_in_string(s: str) -> int:
    co = 0
    for i in s.split():
        current = i.strip("%")
        if current == current[::-1] and len(current) > 1:
            co += 1
    return co


with open("exam_task1/in.txt", "r", encoding="utf-8") as file:
    
    first_string = file.readline()
    palindromes = [count_palindromes_in_string(first_string)]
    chars_to_delete = []
    for i in range(len(first_string)):
        if first_string[i] == "%":
            chars_to_delete.append(i)
                    
    number_of_next_line = 1
    
    next_line = file.readline()
    
    while next_line:
        palindromes.append(count_palindromes_in_string(next_line))
        for j in chars_to_delete:
            if next_line[j+number_of_next_line*1] == "%":
                continue
            else:
                chars_to_delete.remove(j)
        number_of_next_line +=1 
        next_line = file.readline()
        
    
        
with open("exam_task1/in.txt", "r", encoding="utf-8") as f, open("exam_task1/out.txt", "w", encoding="utf-8") as o:
    n = 0
    string = f.readline()
    while string:
        char_list = list(string)
        for i in chars_to_delete[::-1]:
            char_list.pop(i + n)
        
        res = "".join(char_list).strip("\n") + " " + str(palindromes[n]) + "\n"
        o.write(res)
        n += 1
        string = f.readline()
     