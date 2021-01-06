  
import os

#Nhập tên và loại file
file = input('Nhập tên file muốn tạo:')
type = input('Thể loại file:')
file = file + '.'+ type

#Nhập nội dung file
f = open(file, mode = 'w')
f.write(input('Nhập nội dung:'))
f.close()
#Nhập đường dẫn 
folder = input('Nhập đường dẫn của thư mục mà bạn muốn lưu lại:')
h = folder+'\\'+file

#Lưu lại file vào đường dẫn đã nhập
os.rename(file,h)