import struct
import random


with open("binary_bubblesort/numbers.bin", "wb") as file:
    
    for i in range(15):
        num = struct.pack("q", random.randint(0,15))
        file.write(num)


with open("binary_bubblesort/numbers.bin", "r+b") as file:
    file.seek(0,2)
    length = file.tell()//8
    file.seek(0)
    for i in range(0, length):
        swapped = False
        for j in range(0, length - i - 1):
            file.seek(j*8)
            num1 = struct.unpack("q", file.read(8))[0]
            file.seek((j+1)*8)
            num2 = struct.unpack("q", file.read(8))[0]
            if num1 > num2:
                file.seek(j*8)
                file.write(struct.pack("q", num2))
                
                file.seek((j + 1) * 8)
                file.write(struct.pack("q", num1))
        if not swapped:
            break

with open("binary_bubblesort/numbers.bin", 'rb') as file:
    lst = []
    number = file.read(8)
    while number:
        num = struct.unpack("q", number)[0]
        lst.append(num)   
        number = file.read(8)     
    print(*lst)