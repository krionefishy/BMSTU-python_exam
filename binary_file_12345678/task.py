import struct
import random

input_file = "binary_file_12345678/numbers.bin"

def change_numbers(filename, start, end):
    with open(filename, "r+b") as file:
        while start < end:
            file.seek(start*8)
            num1 = file.read(8)
            
            file.seek(((end-1)*8))
            num2 = file.read(8)
            
            file.seek(((end-1)*8))
            file.write(num1)
            
            file.seek(start*8)
            file.write(num2)
            
            start += 1
            end -= 1


with open(input_file, "wb") as file:
    
    for i in range(1,9):
        num = struct.pack("q", i)
        file.write(num)
                    
                    
                    
with open(input_file, "rb") as file:
    file.seek(0,2)
    length = file.tell() // 8
    file.seek(0)
    change_numbers(input_file,0,length)
    change_numbers(input_file,0,length//2)
    number = file.read(8)
    res = []
    while number:
        res.append(struct.unpack("q", number)[0])
        number = file.read(8)
        
    print(*res)