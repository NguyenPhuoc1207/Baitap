import numpy as np
import random

def phuoc( n ):
    print( " Random ma trận cấp n có định thức khác 0 " )
    while True:
        a = np.random.randint( 10 , size=(n,n) )
        det = np.linalg.det( a )
        AA = a @ a
        AAA = a @ a @ a
        rank_a = np.linalg.matrix_rank( a )
        if det!= 0:
            print('A=', a)
            print("del(A)=", det)
            print("A^A", AA)
            print("A^A^A", AAA)
            
            break
    return( a, det , rank_a , AA , AAA)    
    print( a )
while True:
    n = int(input("Nhập n: "))
    if n>0:
       break
    else:
        print( " nhap lai cap cua ma tran!!! " )
phuoc(n)
     
