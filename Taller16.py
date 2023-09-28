x=[0,1,2,3,4,5,6,7]
y=[7,5,6,3,4,2.5,2,0.5]
xy=0
xEl2=0
sumx=0
sumy=0

for i in range(0,len(x)):
    sumx=float(sumx+x[i])
    
for i in range(0,len(x)):
    sumy=float(sumy+y[i])

for i in range (0,len(x)):
    xy=float(xy+x[i]*y[i])
    
for i in range (0,len(x)):
    xEl2=float(xEl2+(x[i])**2)
    
promx=sumx/(len(x))
promy=sumy/(len(y))

a1=(len(x)*xy-sumx*sumy)/(len(x)*xEl2-(sumx)**2)
print(f"a1: {a1}")
a2=promy-a1*promx
print(f"a2: {a2}")

print(f"\necuación: y= {a2} + {a1}x")

