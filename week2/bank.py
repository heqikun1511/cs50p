import sys

greeting=input("Greeting:")
if greeting.startswith('hello'):
    print('$0')
elif greeting.startswith('hey'):
    print('$20')
else:
    print('$100')