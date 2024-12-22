from math import sqrt
file1 = "exam_task5/in1.txt"
file2 = "exam_task5/in2.txt"
out = "exam_task5/out.txt"
with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2, open(out, "w", encoding="utf-8") as o:
    string = f1.readline()
    while string:
        string = int(string)
        for i in range(string):
            s = f2.readline()
        num1, num2 = map(int, s.split())
        s = num1 + num2 
        if sqrt(s) == int(sqrt(s)):
            o.write(str(s)+"\n")
        
        string = f1.readline()
        f2.seek(0)
