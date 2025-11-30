
a=[2,11,4,1,8,6,9]
b=len(a)


for i in range(b-1):
   for j in range(b-1):
       if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]
print(a)
