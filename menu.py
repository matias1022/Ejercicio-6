import os
from claseFecha import FechaHora

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self):
          os.system('cls')
          salir = False

          while salir == False:
              print('1-\tSumar dos objetos de la clase FechaHora,')
              print('2-\tRestar dos objetos de la clase FechaHora')
              print('3-\tDistinguir entre dos objetos FechaHora cuál es mayor')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1: 
                  print ("Ingresar la primera Fecha y Hora")
                  d=int(input("Ingrese Dia: "))
                  mes=int(input("Ingrese Mes: "))
                  a=int(input("Ingrese Año: "))
                  h=int(input("Ingrese Hora: "))
                  m=int(input("Ingrese Minutos: "))
                  s=int(input("Ingrese Segundos: "))  
                  unaFecha= FechaHora(d,mes,a,h, m, s)
                  unaFecha.Mostrar()
                  
                  print ("Ingresar la segunda Fecha y Hora")
                  d2=int(input("Ingrese Dia: "))
                  mes2=int(input("Ingrese Mes: "))
                  a2=int(input("Ingrese Año: "))
                  h2=int(input("Ingrese Hora: "))
                  m2=int(input("Ingrese Minutos: "))
                  s2=int(input("Ingrese Segundos: "))
                  segundaFecha=FechaHora(d2,mes2,a2,h2, m2, s2)
                  segundaFecha.Mostrar()
                  suma=unaFecha+segundaFecha
                  print("El Resultado total en Segundos es: ",suma)
              elif self.__op == 2: 
                  print ("Ingresar la primera Fecha y Hora")
                  d=int(input("Ingrese Dia: "))
                  mes=int(input("Ingrese Mes: "))
                  a=int(input("Ingrese Año: "))
                  h=int(input("Ingrese Hora: "))
                  m=int(input("Ingrese Minutos: "))
                  s=int(input("Ingrese Segundos: "))  
                  unaFecha= FechaHora(d,mes,a,h, m, s)
                  unaFecha.Mostrar()
                  
                  print ("Ingresar la segunda Fecha y Hora")
                  d2=int(input("Ingrese Dia: "))
                  mes2=int(input("Ingrese Mes: "))
                  a2=int(input("Ingrese Año: "))
                  h2=int(input("Ingrese Hora: "))
                  m2=int(input("Ingrese Minutos: "))
                  s2=int(input("Ingrese Segundos: "))
                  segundaFecha=FechaHora(d2,mes2,a2,h2, m2, s2)
                  segundaFecha.Mostrar()
                  resta=unaFecha+segundaFecha
                  print("El resultado de las resta expresada en segundos es:")
                  print (resta)
              elif self.__op == 3: 
                  print ("Ingresar la primera Fecha y Hora")
                  d=int(input("Ingrese Dia: "))
                  mes=int(input("Ingrese Mes: "))
                  a=int(input("Ingrese Año: "))
                  h=int(input("Ingrese Hora: "))
                  m=int(input("Ingrese Minutos: "))
                  s=int(input("Ingrese Segundos: "))  
                  unaFecha= FechaHora(d,mes,a,h, m, s)
                  unaFecha.Mostrar()
                  print ("Ingresar la segunda Fecha y Hora")
                  d2=int(input("Ingrese Dia: "))
                  mes2=int(input("Ingrese Mes: "))
                  a2=int(input("Ingrese Año: "))
                  h2=int(input("Ingrese Hora: "))
                  m2=int(input("Ingrese Minutos: "))
                  s2=int(input("Ingrese Segundos: "))
                  segundaFecha=FechaHora(d2,mes2,a2,h2, m2, s2)
                  segundaFecha.Mostrar()   
                  if unaFecha>segundaFecha:
                      print ("La primera fecha es mas grande que la segunda")
                  else: print("La segunda fecha es mas grande que la primera")
              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')  

if __name__ == '__main__':
    ObjetoMenu = Menu()
    ObjetoMenu.Ejecutar() 