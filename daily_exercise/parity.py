def main():
    x=int(input('what is x'))
    if even(x):
        print('even')
    else:
        print('odd')

def even(n):
    return True if n%2==0 else False


main()