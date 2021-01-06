import random
import string

n = random.randint(50, 100) 
print('Số phần tử trong mỗi list hiện tại:',n)

list1 = []

for i in range(n):
    

    n = random.randint(1,15)
    name = random.choice(string.ascii_uppercase) 
    for i in range(n):
        name += random.choice(string.ascii_lowercase)
        
    n = random.randint(0, 150)  

    dic = {'name':name,'age':n} 
    list1.append(dic)         
    
print('List =',list1)