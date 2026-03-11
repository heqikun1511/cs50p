import sys
def main():
    camel=input('camelcase').strip()
    print('snakename:',end=' ')
    for word in camel:
        if word.isupper():
            print("_"+word.lower(),end='')
        else:
            print(word,end="")

main()