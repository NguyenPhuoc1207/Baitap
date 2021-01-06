
import random
import string

#Tạo giá trị cho name
n = random.randint(1,15)
name = random.choice(string.ascii_letters)
for i in range(n):
    name += random.choice(string.ascii_lowercase)
    
#Tạo giá trị ngẫu nhiên cho age
n = random.randint(0, 150)
dic = {'name':name,'age':n}
print('Dictionary vừa tạo:',dic)