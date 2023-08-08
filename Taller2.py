def union(A, B):
    C=A.union(B)
    return C

def inter(A, B):
    C = A.intersection(B)
    return C

def dif(A, B):
    C = A.difference(B)
    return C

def difSim(A, B):
    C = A.symmetric_difference(B)
    return C

cont=0

A=set()
for i in range(26):
    if i% 2==1:
        A.add(i)

print(A)

B=set()
for i in range (6,20):
    B.add(i)

print(B)

C=set({1,4,7,8,12,16,18,21})

print(C)

D=set()
for i in range (51):
  for x in range(1,i):
    if (i%x) == 0:
      cont+=1
  if cont==1:
   D.add(i)
  cont=0
  
print(D)

re=(inter(A, difSim(B,D)))
print("\nOp1:")
print(re)

re=(union(inter(B,C), D))
print("\nOp2:")
print(re)

re=(dif(union(A,C), B))
print("\nOp3:")
print(re)

re=(difSim(dif(B,C), inter(A,C)))
print("\nOp4:")
print(re)