input_file1 = "merge_two_sorted_lists/in1.txt"
input_file2 = "merge_two_sorted_lists/in2.txt"
output_file = "merge_two_sorted_lists/out.txt"
with open(input_file1, "r", encoding="utf-8") as f1, open(input_file2, "r", encoding="utf-8") as f2, open(output_file, "w", encoding="utf-8") as o:
    n1 = f1.readline().strip("\n")
    n2 = f2.readline().strip("\n")
    while n1 and n2:
        n1 = int(n1)
        n2 = int(n2)
        if n2 >= n1:
            o.write(f"{n1}\n")
            n1 = f1.readline().strip("\n")
        else:
            o.write(f"{n2}\n")
            n2 = f2.readline().strip("\n")

    while n1:
        o.write(f"{n1}\n")
        n1 = f1.readline().strip("\n")
    while n2:
        o.write(f"{n2}\n")
        n2 = f2.readline().strip("\n")