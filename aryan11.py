d1,d2,d3=map(int,input().split())
r1=d1+d2+d3
r2=(d1+d2)*2
r3=(d3+d2)*2
r4=(d1+d3)*2
if r1<=r2:
    if r1<=r3:
        if r1<=r4:
            print(r1)
        else:
            print(r4)
    else:
        if r3<=r4:
            print(r3)
        else:
            print(r4)
elif r2<=r1:
    if r2<=r3:
        if r2<=r4:
            print(r2)
        else:
            print(r4)
    else:
        if r3<=r2:
            print(r3)
        else:
            print(r2)
elif r3<=r1:
    if r3<=r2:
        if r3<=r4:
            print(r3)
        else:
            print(r4)
    else:
        if r2<=r3:
            print(r2)
        else:
            print(r3)
elif r4<=r1:
    if r4<=r2:
        if r4<=r3:
            print(r4)
        else:
            print(r3)
    else:
        if r2<=r4:
            print(r2)
        else:
            print(r4)
