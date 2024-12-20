import struct
import random


with open("sort_binary/numbers.bin", "wb") as file:
    
    for i in range(15):
        num = struct.pack("q", random.randint(0,15))
        file.write(num)


with open("sort_binary/numbers.bin", "r+b") as file:
    file.seek(0,2)
    length = file.tell() // 8
    file.seek(0)
    for i in range(length - 1):
        
        file.seek(i*8)
        min_index = i
        mn_num = struct.unpack("q", file.read(8))[0]
        
        for j in range(i+1, length):
            
            file.seek(j * 8)
            num2 = struct.unpack("q", file.read(8))[0]
            
            if num2 < mn_num:
                min_index = j
                mn_num = num2
                
        if min_index != i:
            file.seek(i * 8)
            curr_val = struct.unpack('q', file.read(8))[0]
           
            file.seek(i * 8)
            file.write(struct.pack("q", mn_num))
            
            file.seek(min_index*8)
            file.write(struct.pack("q", curr_val))
            
            
            
with open("sort_binary/numbers.bin", 'rb') as file:
    lst = []
    number = file.read(8)
    while number:
        num = struct.unpack("q", number)[0]
        lst.append(num)   
        number = file.read(8)     
    print(*lst)