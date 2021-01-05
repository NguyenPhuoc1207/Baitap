
import math
list = [0 , -5 , 60.5 , 1 , 0.5]
print(list)
print('Giá trị của phần tử và logarit tương ứng:')
for i in list:

  if i <= 0:
    print(i , ', Không có logarit tương ứng.')
  else:
    print(i , ', logarit của' , i , ':' , math.log(i))
