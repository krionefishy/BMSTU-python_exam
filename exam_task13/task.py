import struct 

def hex_to_oct(x: str):
    if "," in x:
        l = x.split(",")
        if len(l) == 2:
            left, right = l 
        else:
            left = l[0]
            right = 0
        left_oct = oct(int(left, 16))[2:]
        right_oct = oct(int(right, 16))[2:]
        return left_oct + "," + right_oct
    
    else:
        return oct(int(x, 16))[2:]

def check_if_valid(x: str):
    ALPH = "0123456789abcdef,-"
    if (x.count("-") > 1) or (x.count(",") > 1) or (not all(j.lower() in ALPH for j in x)) or \
        (x.count("-") == 1 and x.index("-") != 0) or (x == ",") or (x == "-"):
        return False 
    return True 

print(check_if_valid("A,A"))
print(check_if_valid("-A,15"))
print(check_if_valid("abc"))
print(check_if_valid("45"))
print(check_if_valid("1-8"))
print(check_if_valid("B,"))
print(check_if_valid(",abc"))

with open("exam_task13/in.txt", "r", encoding="utf-8") as f, \
    open("exam_task13/out.txt", "w", encoding="utf-8") as o:
        s = f.readline().strip("\n")
        co_s = 0
        co_w = []
        words_in_current = 0
        while s:
            cur = s.split()
            for ind in range(len(cur)):
                words_in_current += 1
                
                if "." in cur[ind]:
                    if check_if_valid(cur[ind][:-1]):
                        if "-" in cur[ind]:
                            res = "-" + hex_to_oct(cur[ind][1:-1])
                        else:
                            res = hex_to_oct(cur[ind][:-1])
                        cur[ind] = res + "."
                    co_s += 1
                    co_w.append(words_in_current)
                    words_in_current = 0
                elif check_if_valid(cur[ind]):
                    if "-" in cur[ind]:
                        res = "-" + hex_to_oct(cur[ind][1:])
                    else:
                        res = hex_to_oct(cur[ind])
                    cur[ind] = res 
            string_to_write = " ".join(cur) + "\n"
            o.write(string_to_write)
            s = f.readline().strip("\n")                                  
        

with open("sent.bin", "wb") as b:
    b.write(struct.pack("h", co_s))
    for i in range(co_s):
        b.write(struct.pack("h", co_w[i]))
        
        
with open("sent.bin", "rb") as b:
    s = b.read(struct.calcsize("h"))
    print(f"Количество предложений в файле равно: {co_s}")
    print("Количество слов в каждом предложении:")
    for i in range(co_s):
        print(struct.unpack("h", b.read(struct.calcsize("h")))[0], end = " ")