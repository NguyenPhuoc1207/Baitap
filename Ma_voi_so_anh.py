import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
np.set_printoptions(suppress=True)

a = np.random.randint(-100, 100, size=(3, 4))
print(a)

u, s, v = np.linalg.svd(a)
print(u)
print("-"*50)
print(s)
print("-"*50)
print(v)
print("-"*50)
sigma = np.zeros((3, 4))
print(sigma)
for i, x in enumerate(s):
    sigma[i, i] = x
print(sigma)
#print(np.array([[*s[:], 0]))
b = u@sigma@v
print(b)
print(a-b)
M=np.zeros((3,4))
M[0,2]=10
print(M)
pic=Image.open('Nhu_Quynh.JPG')
plt.imshow(pic)
plt.imshow(pic, cmap='gray')
plt.plot(s, 's-')
#plt.xlim([o,300])
#plt.ylim([500,3000])
plt.xlabel('số thành phần')
plt.ylabel('Giá trị suy biến')
plt.show()