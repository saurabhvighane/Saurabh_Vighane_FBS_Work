path = 'WNEENSENNN'
x=0
y=0
for ch in path:
    if ch=='N':
        y+=1
    elif ch=='S':
        y-=1
    elif ch=='E':
        x+=1
    elif ch=='W':
        x-=1
    else:
        print("Invalid path")

dist=((x**2)+(y**2))**0.5

print("Total distance travled:",dist)