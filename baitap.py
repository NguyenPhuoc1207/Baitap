import numpy as np  
from sympy import  Matrix
def matran(m, n):
    a = np.random.randint(-10000, 10000, size = (m, n))
    print (" A = ",a)
    return(a)

def rank_matran(a):
    rank_a = np.linalg.matrix_rank(a)
    print("rank(A) = ",rank_a)
    return(rank_a)
def ma_tran_bac_thang(a): 
    ma_tran_bac_thang=Matrix(a).rref()
    print("ma_tran_bac_thang", ma_tran_bac_thang)


ma_tran_bac_thang(matran(3, 4))
     
    
    