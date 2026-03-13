import sys
a=input('Input:').strip()
standards="aeiouAEIOU"
result=""
for i in a:
    if i not in standards:
        result+=i
print(result)
