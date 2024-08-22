def fun(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            value=input()
            row.append(value)
        matrix.append(row)
    print(matrix)
fun(3)
