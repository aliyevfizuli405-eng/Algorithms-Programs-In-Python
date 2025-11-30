Fizuli=[66,31,69,3,5]
c=len(Fizuli)
d=[]

for i in range(c):
    d.append(min(Fizuli))
    Fizuli.remove(min(Fizuli))
print(d)
