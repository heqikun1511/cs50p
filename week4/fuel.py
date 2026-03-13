import sys
Fraction=input("Fraction:").strip()
x,y=Fraction.split('/')
x_int=int(x)
y_int=int(y)
per=round((x_int/y_int)*100)
if per<=1:
    print('E')
elif per>=99:
    print('f')
else:
    print(f"{per}%")