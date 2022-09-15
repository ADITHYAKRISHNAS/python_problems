f1=open("R.jfif",'rb')
f2=open("RCopy.jfif",'wb')
for i in f1:
    print(f2.write(i))
