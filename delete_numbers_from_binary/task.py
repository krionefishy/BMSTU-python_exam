import struct

input_file = "delete_numbers_from_binary/numbers.bin"
output_file = "numbers_odd.bin"

with open(input_file, 'wb') as f:
    numbers_to_write = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numbers_to_write:
        f.write(struct.pack('q', num))


# bad solution, because of using extra space (bin bin agritsa)
'''with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
    while True:
        try:
            number = infile.read(8)
            if not number:
                break
            num = struct.unpack('q', number)[0] 

            if num % 2 != 0: 
                outfile.write(number)
        except struct.error:
            break'''
        
        
        
with open(input_file, "r+b") as f:
    current_position = 0
    count_odd = 0
    number = f.read(8)
    if not number:
        print("файл пустой")
    else:
        while number:
                num = struct.unpack('q', number)[0]
                current_position = f.tell()             
                if num % 2 != 0:
                    count_odd += 1
                    f.seek((count_odd-1)*8)
                    n = struct.pack('q', num)
                    f.write(n)
                    f.seek(current_position)
                number = f.read(8)          
        f.truncate(count_odd*8)
        
with open(input_file, "rb") as f:
    number = f.read(8)
    while number:
        num = struct.unpack('q', number)[0]
        print(num)
        number = f.read(8)