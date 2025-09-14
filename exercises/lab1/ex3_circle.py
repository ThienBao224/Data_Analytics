import sys, math

if len(sys.argv) < 2:
    print("Ban phai nhap ban kinh khi chay chuong trinh")
else:
    r = float(sys.argv[1])
    cv = 2 * math.pi * r
    dt = math.pi * r ** 2

    print("Ban kinh r =", r)
    print("Chu vi =", cv)
    print("Dien tich =", dt)
