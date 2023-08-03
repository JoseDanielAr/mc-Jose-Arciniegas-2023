G1=set()
G2=set()
switch=0

#Ingresar numeros
while switch==0:
    x=float(input("Ingrese un numero decimal para el grupo 1\n"))
    G1.add(x)
    R=int(input("¿Añadir otro numero al grupo 1\n1. Sí\n2. No\n"))
    if R!=1:
        switch=1

switch=0

print("El grupo 1 es: ", G1 ,"\n")
while switch==0:
    x=float(input("Ingrese un numero decimal para el grupo 2\n"))
    G2.add(x)
    R=int(input("¿Añadir otro numero al grupo 2\n1. Sí\n2. No\n"))
    if R!=1:
        switch=1

switch=0

print("El grupo 2 es: ", G2)

#Operaciones
while switch==0:
    R=int(input("\nSeleccione la operación\n1. Union\n2. Intersección\n3. Diferencia (conjunto 1 - conjunto 2)\n4. Diferencia simetrica\n")) 

    if R==1:
        print(G1.union(G2))
        R=int(input("¿Realizar otra operación?\n1: Sí\nOtro valor: No\n"))
        if R!=1:
         switch=1
    elif R==2:
        print(G1.intersection(G2))
        R=int(input("¿Realizar otra operación?\n1: Sí\nOtro valor: No\n"))
        if R!=1:
         switch=1
    elif R==3:
        print(G1.difference(G2))
        R=int(input("¿Realizar otra operación?\n1: Sí\nOtro valor: No\n"))
        if R!=1:
         switch=1
    elif R==4:
        print(G1.symmetric_difference(G2))
        R=int(input("¿Realizar otra operación?\n1: Sí\nOtro valor: No\n"))
        if R!=1:
         switch=1
    else:
        print("Comando invalido")


