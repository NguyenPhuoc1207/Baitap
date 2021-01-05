import random
while True: 
  n = int(input('Số lượng phần tử trong dãy:'))   
  list = [] 
  if n == 0:
    print(list, 'Dãy không có phần tử nào. Không có giá trị nhỏ nhất.')
  elif n > 0:
    for i in range(n):
      list.append(random.random())   
    min = list[0]                    
    for i in range(n):
      if min > list[i]:
        min = float(list[i])
    print(list) 
    print('Phần tử nhỏ nhất trong dãy trên là:' , min) 
  print('*Vui lòng nhập số nguyên dương.*')

  option = input("-Bạn có muốn tiếp tục không?(y/n) ")
  if option == 'n' or option == 'N':
      print('Finish!')
      break  