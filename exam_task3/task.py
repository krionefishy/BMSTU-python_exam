import re
def find_all_numbers(s: str) -> int:
    co = len(re.findall(r'-?\d+([.,]\d+)?([eE][-+]?\d+)?', s))
    return co


with open("exam_task3/in.txt", "r", encoding="utf-8") as file, open("exam_task3/out.txt", "w", encoding="utf-8") as o:
    count_of_numbers = []
    s = file.readline()
    count_of_numbers.append(find_all_numbers(s))
    chars_to_delete = []
    for i in range(len(s)):
        if s[i] == "#":
            chars_to_delete.append(i)
        

    next_line = file.readline()
    while next_line:
        count_of_numbers.append(find_all_numbers(next_line))
        for i in chars_to_delete:
            if next_line[i] != "#":
                chars_to_delete.remove(i)
        next_line = file.readline()

    
    file.seek(0)
    s = file.readline()
    n = 0
    while s:
        chrs = list(s)
        for i in chars_to_delete[::-1]:
            chrs.pop(i)
        res = "".join(chrs).strip("\n") + " " + str(count_of_numbers[n]) + "\n"
        o.write(res)
        s = file.readline()
        n += 1
