import os

list1=[]
list2=[]

'''2)Lập trình đọc tất cả tập tin 
và thư mục con trực tiếp của thư mục gốc ổ đĩa C và in kết quả ra màn hình'''
for (root,dirs,files) in os.walk('C:\\', topdown=True):
    list2 += dirs
    list1 += files
    print(root)
    print(dirs)
    print(files)
    print('--------------------------------')
    
'''3)Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và:
      - Danh sách tập tin đưa vào List1
      - Danh sách thư mục đưa vào List2'''
print('Danh sách tất cả các thư mục:',list2)
print('--------------------------------')
print('Danh sách tất cả các tập tin:',list1)