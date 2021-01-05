import random
while True: 
  n = int(input('Số lượng phần tử trong dãy:'))
  list = [] 
  if n == 0:
    print(list, 'Dãy không có phần tử nào. Không có giá trị lớn nhất.')
  elif n > 0:
    for i in range(n):
      list.append(random.random())
    max = list[0]                    
    for i in range(n):
      if max < list[i]:
        max = float(list[i])
    print(list) 
    print('Phần tử lớn nhất trong dãy trên là:' , max)
  print('*Vui lòng nhập số nguyên dương.*')
  option = input("-Bạn có muốn tiếp tục không?(y/n) ")
  if option == 'n' or option == 'N':
      print('Finish!')
      break  
