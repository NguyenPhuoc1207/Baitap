import numpy as np
def matran( m, n ):
    
        a=np.random.randint(10 , size=(m,n))
        rank_a = np.linalg.matrix_rank( a )
        return( a, rank_a)
        print("a", a)
        print("rank_a", rank_a)       
matran(2, 3)    
         
    
        
        
    