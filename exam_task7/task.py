import struct
from math import sqrt

def delete_current(filename, num, n):
    with open(filename, "r+") as file:
        file.seek(n * size * (num + 1))
        s = file.read(size*n)
        while s:
            file.seek(n * size * (num))
            file.write(s)
            num += 1
            file.seek(n * size * (num + 1))
            s = file.read(n * size)
            
        file.truncate(n * n * size - n*size)
        
        

            
num_format = "q"
size = struct.calcsize(num_format)
with open("exam_task7/in.bin", "wb") as file:
    for i in range(5):
        for j in range(5,0,-1):
            file.write(struct.pack(num_format, j))
          
with open("exam_task7/in.bin", "rb") as file:
    s = file.read(8)
    c = 0
    temp = ""
    while s:
        if c == 5:
            print(temp)
            c = 0
            temp = ""
            
        temp += str(struct.unpack(num_format, s)[0])
        c += 1
    
        s = file.read(size)
    print(temp)
    
print()  
        
        
with open("exam_task7/in.bin", "r+b") as file:
    file.seek(0,2)
    n = int(sqrt(file.tell()//8))
    
    
    for i in range(n):
        for j in range(i + 1, n):
            pos1 = (i * n + j) * 8
            pos2 = (j * n + i) * 8
            
            file.seek(pos1)
            el1 = file.read(size)
            file.seek(pos2)
            el2 = file.read(size)

            file.seek(pos1)
            file.write(el2)
            file.seek(pos2)
            file.write(el1)

            
            
        
with open("exam_task7/in.bin", "rb") as file:
    s = file.read(8)
    c = 0
    temp = ""
    while s:
        if c == 5:
            print(temp)
            c = 0
            temp = ""
            
        temp += str(struct.unpack(num_format, s)[0])
        c += 1
    
        s = file.read(size)
    print(temp)

print()
        
        
        
with open("exam_task7/in.bin", "r+b") as file:
    mx = 0
    current = 0
    for i in range(n):
        temp = 0
        for j in range(n):
            s = file.read(size)
            temp += struct.unpack(num_format, s)[0]
        if temp > mx:
            mx = temp
            current = i
            
    file.seek(0)
    if current == n - 1:
        file.truncate(n * n * size - n*size)
    else:
        delete_current("exam_task7/in.bin", current, n)

with open("exam_task7/in.bin", "rb") as file:
    s = file.read(8)
    c = 0
    temp = ""
    while s:
        if c == 5:
            print(temp)
            c = 0
            temp = ""
            
        temp += str(struct.unpack(num_format, s)[0])
        c += 1
    
        s = file.read(size)
    print(temp)