

a = float(input("a="))
b = float(input("b="))
if a == 0:
    b == 0
    print("phuong trinh co vo so nghiem")
else:
    x = -b / a
    counter = 1

    n = int(input("n="))

    while counter <= n:
        print("phuong trinh co nghiem la", x, counter)
counter += 1
print("ket thuc")