import struct
import random


with open("binary_sort_insertion/numbers.bin", "wb") as file:
    
    for i in range(15):
        num = struct.pack("q", random.randint(0,15))
        file.write(num)

    
    

with open("binary_sort_insertion/numbers.bin", "r+b") as file:
    file.seek(0,2)
    length = file.tell() // 8
    file.seek(0)
    for i in range(1,length):
        file.seek(i * 8)
        num = struct.unpack("q", file.read(8))[0]
        j = i - 1
        file.seek(j*8)
        num2 = struct.unpack("q", file.read(8))[0]
        
        while num2 > num and j >= 0:
            file.seek((j+1)*8) 
            file.write(struct.pack("q", num2))
            j -= 1
            if j >= 0:
                file.seek(j*8)
                num2 = struct.unpack("q", file.read(8))[0]
                
        file.seek((j+1)*8) 
        file.write(struct.pack("q", num))
        





with open("binary_sort_insertion/numbers.bin", 'rb') as file:
    lst = []
    number = file.read(8)
    while number:
        num = struct.unpack("q", number)[0]
        lst.append(num)   
        number = file.read(8)     
    print(*lst)