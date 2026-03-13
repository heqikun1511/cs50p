import sys
from pyfiglet import Figlet
import random

def main():
    figlet=Figlet()
    fonts=figlet.getFonts()
    if len(sys.argv)==1:
        font=random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv)==3:
        if sys.argv[1] not in ('-f,''--font'):
            sys.exit("invalid")
        if sys.argv[2] not in fonts:
            sys.exit("invalid")
        figlet.setFont(Font=sys.argv[2])
    else:
        sys.exit("invalid")
    text=input('Input:')
    print(figlet.renderText(text))

main()

