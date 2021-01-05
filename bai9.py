import os
import time
while True :
    check = input("Bạn muốn tắt máy không ? (y/n): ");
    if check == 'n' or check == 'N':
        print('Sẽ hỏi lại sau:')
        for c in range(1 , 31):
            print(c, end=' ')
            time.sleep(1) #Hen gio tat may (30s)
    else:
        os.system("shutdown /s /t 1");
        break