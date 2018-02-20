import math
lista=[]
X=[]
indices=[]
def alpinista(x):

   global indices,X
   for i in range(0,x+1):
       X.append(i)
   #print(X)

   for i in range(0,len(X)):
       actual=X[i]
       vecino=X[actual+1]

       #print("*"*20)
       #print("Actual ",actual)
       #print("Vecino ",vecino)

       f_actual=0.0
       f_vecino=0.0

       f_actual=math.sin(actual/10)
       f_vecino=math.sin(vecino/10)
       #print("F actual",f_actual)
       #print("F vecino",f_vecino)
       #print("Verificacion",f_actual > f_vecino)

       if  f_vecino >= f_actual :
           #print("Actual ",math.sin(actual/10))
           #print("Vecino " ,math.sin(vecino/10))
           lista.append(f_actual)
           indices.append(actual)
           actual=vecino



           #print("cumple")
       if i == len(X)-2:
            break
   return lista


minimo=min(alpinista(50))
#print("lista de indices",indices)
#print(minimo)
indice_lista_minimos=lista.index(minimo)
valor=indices[indice_lista_minimos]
print("F minima es : ",minimo)
print("El valor de x que lo vuelve minimo es : ",valor)

#indice_menor=indices.index(indice_lista_minimos)
#print(indice_menor)





import math

def Alpinista(x):
  u = 0
  dominio=0
  while (dominio<x+1):
    v = u + 1
    
    V=math.sin(v/10)
    U=math.sin(u/10)
    
    if V <= U:   
        u = v
    else:
        break
    dominio=dominio+1
    if dominio == x-2:
       break
    
  print("El valor que hace minima a la funcion es {0} y el valor minimo es {1}".format(u,U))
  
Alpinista(50)
