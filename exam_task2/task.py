def right(k1: int, k2: int):
    global matrix, max_koord
    if k2 + 1 <= max_koord:
        return matrix[k1][k2+1], k1, k2+1
    return None, -1, -1 


def left(k1: int, k2: int):
    global matrix
    if k2 - 1 >= 0:
        return matrix[k1][k2-1], k1, k2-1
    return None, -1, -1
    
    
def up(k1: int, k2: int):
    global matrix
    if k1 - 1 >= 0:
        return matrix[k1-1][k2], k1 - 1, k2 
    return None, -1, -1
    
def down(k1: int, k2: int):
    global matrix, max_koord
    if k1 + 1 <= max_koord:
        return matrix[k1+1][k2], k1 + 1, k2
    return None, -1, -1
    
    
def go_by_direction(drct, k1, k2):
    global path
    match drct:
        case ">":
            nxt, c1, c2 = right(k1,k2)
        case "<":
            nxt, c1, c2 = left(k1,k2)
        case "^": 
            nxt, c1, c2 = up(k1,k2)
        case "v":
            nxt, c1, c2 = down(k1,k2)
        case _:
            return "end"
    if (k1,k2) in path[-1]:
        return "end"
    path[-1].append((k1,k2))
            
    if nxt is None:
        return "end"
            
    return go_by_direction(nxt, c1, c2)
path = [[]]


with open("exam_task2/in.txt", "r", encoding="utf-8") as file:
    matrix = [i.strip().split() for i in file.readlines()]
    max_koord = len(matrix) - 1
    
    
matrix_stolbs = [[] for _ in range(max_koord+1)]

for i in range(max_koord+1):
    for j in range(max_koord+1):
        matrix_stolbs[j].append(matrix[i][j])
        if matrix[i][j] in "><v^":
            ex_code = go_by_direction(matrix[i][j], i, j)
            if ex_code == "end":
                path.append([])
                continue
            
longest_path = max(path, key = lambda x: len(x))

last_string = [len([j for j in longest_path if j[1] == i]) for i in range(max_koord + 1)]

for i in range(max_koord+1):
    matrix_stolbs[i].append(last_string[i])
    
    
res = sorted(matrix_stolbs, key = lambda x: x[-1], reverse= True)


with open("exam_task2/out.txt", "w", encoding="utf-8") as o:
    for i in range(max_koord+1):
        temp = []
        for j in range(max_koord+1):
            temp.append(res[j][i])
            
        o.write(" ".join(temp) + "\n")
        
    o.write(" ".join(list(map(str,sorted(last_string, reverse=True)))))
