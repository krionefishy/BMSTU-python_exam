import struct
s_format = "i"
size = 4
filename = "remove_from_bin/in.bin"


with open(filename, "wb" ) as f:
    for i in range(10):
        f.write(struct.pack("i", i))
        
with open(filename, "rb" ) as f:
    s = f.read(size)
    while s:
        print(struct.unpack(s_format, s)[0], end = " ")
        s = f.read(size)   
        
print()     
        
def remove_nth_elem(filename, n):
    with open(filename, "r+b") as f:
        f.seek((n - 1) * size)
        curr = f.read(size)
        while curr:
            nxt = f.read(size)
            f.seek((n-1) * size)
            f.write(nxt)
            curr = f.read(size)
            n += 1
            
        f.seek(0,2)
        f.truncate(f.tell() - size)
        
        
        
remove_nth_elem(filename, 5)
with open(filename, "rb" ) as f:
    s = f.read(size)
    while s:
        print(struct.unpack(s_format, s)[0], end = " ")
        s = f.read(size)