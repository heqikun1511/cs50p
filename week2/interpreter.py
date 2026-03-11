def main():
    expression=input("Expression").strip()
    x,s,y=expression.split()
    x_str=float(x)
    y_str=float(y)
    out=calucator(x_str,s,y_str)
    print(out)


def calucator(x_str,s,y_str):
    if s=="+":
        return float(x_str+y_str)
    elif s=="-":
        return float(x_str-y_str)




main()