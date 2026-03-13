import sys
grocery={}
while True:
    try:
        item=input().strip().upper()
        if item in grocery:
            grocery[item]+=1
        elif item not in grocery:
            grocery[item]=1
    except EOFError:
        break


for item in sorted(grocery):
    print(f"{grocery[item]},{item}")