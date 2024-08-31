#creo mi clase
class Ejercicios:
    #Metodos
    def suma(self,numero_1,numero_2 ):
        print(numero_1+numero_2)
#definicion de un objeto
ejercicio1 = Ejercicios()
ejercicio2 = Ejercicios()
#llamado de la suma
ejercicio1.suma(numero_1=3,numero_2=5)
ejercicio2.suma(numero_1=6,numero_2=4)

class Area:
   def areatriangulo(self,base,altura):
    print(base*altura/2)
area1 = Area()
area1.areatriangulo(3,4)
