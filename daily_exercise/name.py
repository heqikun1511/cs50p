import sys
name=input('what is your name')
file=open("name.txt","a")
file.write(name)
file.close()
