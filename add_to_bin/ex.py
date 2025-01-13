import struct
s_format = "i"
size = 4
filename = "add_to_bin/in.bin"


with open(filename, "wb" ) as f:
    for i in range(10):
        f.write(struct.pack("i", i))
        
with open(filename, "rb" ) as f:
    s = f.read(size)
    while s:
        print(struct.unpack(s_format, s)[0], end = " ")
        s = f.read(size)   
        
print()     
        
def add_to_nth_pos(filename, n, el):
    with open(filename, "r+b") as f:
        f.seek(0, 2)
        cur = f.tell()
        if n > cur / size:
            f.seek(0,2)
            f.write(struct.pack(s_format, el))
            return 
        pos = n
        f.seek((n-1) * size )
        s = f.read(size)
        while s:
            nxt = f.read(size)
            f.seek(n*size)
            f.write(s)
            n += 1
            s = nxt
        f.seek((pos-1) * size)
        f.write(struct.pack(s_format, el))
        
        
add_to_nth_pos(filename, 5, 15)
with open(filename, "rb" ) as f:
    s = f.read(size)
    while s:
        print(struct.unpack(s_format, s)[0], end = " ")
        s = f.read(size)