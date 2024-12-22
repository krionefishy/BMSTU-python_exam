# btw, we have to read matrix from in.txt, so thats code to read matrix
'''with open("in.txt", "r", encoding="utf-8") as file:
    matr = [list(map(int, line)) for line in file.readlines()]
    '''

matr = [[i for i in range(1,9)] for j in range(1,9)]


def move_one_right(matr, num):
    current = matr[num][num]
    for j in range(num+1,len(matr)-num):
        k = matr[num][j] 
        matr[num][j] = current  
        current = k  

    
    i = len(matr) - num - 1
    for j in range(num +1 ,len(matr)-num):
            k = matr[j][i]
            matr[j][i] = current
            current = k

      

    j = len(matr) - num - 1
    for i in range(len(matr)-2-num, -1+num, -1):
        k = matr[j][i]
        matr[j][i] = current
        current = k    

        
    j = num
    for i in range(len(matr)-2-num, -1 + num, -1):
        k = matr[i][j]
        matr[i][j] = current
        current = k

    
    
def move_one_left(matr, num):
    n = len(matr)
    current = matr[num][n-1-num]
    for j in range(n - num - 2, -1 + num, -1):
        k = matr[num][j]
        matr[num][j] = current
        current = k

    
    j = num 
    for i in range(num + 1, n - num):
        k = matr[i][j]
        matr[i][j] = current     
        current = k

    
    i = n - num - 1
    for j in range(num + 1, n - num ):
        k = matr[i][j]
        matr[i][j] = current
        current = k 

        
    j = n - num - 1    
    for i in range(n-num-2, -1 + num, -1):
        k = matr[i][j]
        matr[i][j] = current
        current = k

    
max_value = max(max(line) for line in matr)
        
for i in range(len(matr) // 2):
    if i % 2 == 0:
        move_one_right(matr, i)
    else:
        move_one_left(matr, i)
        

stolbs_with_max = []
for i in range(len(matr)):
    for j in range(len(matr)):
        if matr[i][j] == max_value:
            if j not in stolbs_with_max:
                stolbs_with_max.append(j)

stolbs_to_write = [i for i in range(len(matr)) if i not in stolbs_with_max]


with open("exam_task4/out.txt", "w", encoding="utf-8") as file:
    for i in range(len(matr)):
        temp = []
        for j in stolbs_to_write:
            temp.append(str(matr[i][j]))
        res = " ".join(temp) + "\n"
        file.write(res)

