coches = {'Bmw':35000, 'Mercedes':45000, 'Toyota':17000, 'Seat':18000, 'Dacia':6700}
def titulo():
     print("\n")
     print("Valoración autómatica de coches")
     print("*******************************\n")


def fordic():

    for clave,valor in coches.items():
       
        print(clave,valor)

        if valor >=33000:
            print("El coche es muy caro \n")
        elif valor >=22000:
            print("El coche es caro\n ")
        elif valor >=7000:
            print("El coche esta bien de precio \n")
        else:
            print("el coche esta barato \n")

        

def formay():   
    
    print("Pasar nombres a mayuscula")
    print("*************************\n")
    for clave, valor in coches.items():
        x = clave.upper()
        print(x+"\n")

titulo()
fordic()
formay()