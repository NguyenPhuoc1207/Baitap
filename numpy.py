import numpy as np

a = np.array([[1,2,3], [4,5,6],[7,8,9]],int) #Tạo ma trận A
b = np.eye(3, dtype=int)                     #Tạo ma trận đơn vị 3x3 B   
c = np.ones((3,2), dtype = int)              #Tạo ma trận C với các phần tử là 1 kích thước 2x2

print('Matrix A :\n',a)
print('Matrix B :\n',b)
print('Matrix C :\n',c)
print('A + B :\n',a + b)  #Tổng 2 ma trận
print('A * C :\n',a @ c)  #Tích 2 ma trận

#Tính ma trận chuyển vị của A:
print('Ma trận chuyển vị của A:\n',np.transpose(a))