  
import string , random , os
def randomstr(): #Tạo hàm để sinh ngẫu nhiên nội dung trong file (kích thước mỗi file:1000KB)
    name = random.choice(string.ascii_letters)
    for i in range(1023999):
        name += random.choice(string.ascii_letters)
    return name
path = input('Nhập đường dẫn nơi bạn muốn tạo thư mục:')+'\\'
path = path + input('Tên thư mục bạn muốn tạo:')
os.mkdir(path)
os.chdir(path)
#Dung lượng dữ liệu giới hạn:
while True:    
    size = float(input('Nhập dung lượng dữ liệu (1MB-1024MB):'))
    if size < 0:
        print('Dung lượng dữ liệu phải là số dương. Vui lòng nhập lại!')
    elif size == 0:
        print('Bạn vừa tạo 1 thư mục rỗng!')
        break
    elif size > 0:
        size = size * 1024 * 1024 #Đổi sang byte
        n =int(size // 1024000) #Số lượng file trong folder
        m =int(size - n * 1024000)  #Số byte còn dư 
#Tạo n file với kích thước mỗi file là 1000KB
        for i in range(n):
            f = 'file'+str(i)+'.txt'
            f = open(f, mode= 'w')
            f.write(randomstr())
            f.close()
#Tạo 1 file với số byte còn lại
        if  m > 0:
            f = 'file'+ str(n) +'.txt'
            f = open(f, mode= 'w')
            name = random.choice(string.ascii_letters)
            for i in range(m - 1):
                name += random.choice(string.ascii_letters)
            f.write(name)
            f.close()
            n += 1
        print('Đã tạo:', n ,'file!')
        break