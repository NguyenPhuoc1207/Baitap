import random

n = random.randint(50, 1000) 
print('Số phần tử trong mỗi list hiện tại:',n)
print('''
            ''')
list1 = []
list2 = []
for i in range(n):
    i = random.randint(-1000, 1000) 
    list1.append(i)         
for i in range(n):
    i = random.uniform(-1000.0, 1000.0) 
    list2.append(i)         
print('List1 =',list1)
print('''
            ''')
print('List2 =',list2)

