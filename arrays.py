def fun(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            value=input()
            row.append(value)
        matrix.append(row)
    for row in matrix:
        print(row)
fun(3)
