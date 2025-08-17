list=[1,4,9,16,25,36,49,64,81,100]
x=49
i=0
while i<len(list):
    if(list[i]==x):
        print("found at bcroy",i)
        break;
    else:
        print("not found")
        i+=1