#Se crea una lista vacia para agregar valores
aprendices = []

# Se crea un ciclo for, el cual tiene un rango de 30, este ciclo registrara los datos del estudiante, y al llegar al registro 30(29) directamente preguntara por el instructor y se registrara en la lista, estos tienen el .title para tener la primera mayuscula, y los valores estan concatenados en un string para que queden como un solo elemento en la lista
for i in range(30):
    nombre = input("Introduce un nombre: ").title()
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices.append(nombre + " " + str(edad))
    if i == 29: 
      nombre = input("Introduce el nombre del tu instructor: ").title()
      edad = int(input(f"Introduce la edad de {nombre}: "))
      instru = (nombre + " " + str(edad))
      aprendices.insert(0,instru) #Aqui ponemos la variable instru con el valor de nombre y edad en el indice (index) 0 para que sea el primero en la lista
      break

#Empezamos a realizar las muestras de la lista, aqui hacemos uso de la clase enumerate, que se almacena en i, y el elemento que sera cada valor de la lista.
print("\nLista de aprendices\n")
for i, elemento in enumerate(aprendices):
    print(f"# {i + 1}: {elemento}")

#Aqui creo otra lista que tendra la principal ordenada, esto era para que no desordenara el primer ejercicio.
lista=(sorted(aprendices))

#La siguiente pregunta es para hacer una serie de pasos, ejemplo ver los aprendices con 18, el mas viejo y luego pasar a mas procesos, si la persona no digita s saltara de pasos hasta el ciclo while.
pre=(input("\nQuieres ver cuantos aprendices tienen 18 y cual es el mas longevo? s/n: " ).lower())

#El siguiente if verifica que se haya dicho "s", luego de esto mediante la sentencia split, vamos a separar por espacios los valores de la lista, y vamos a sacar la edad en todos los ejercicios con el split -1, ya que es el unico valor de la lista, asi nos ahorramos problemas de si la persona tiene 2 nombres o 3
if pre == "s":
  nAprend = None
  eAprend= 0
  for i in lista:
      nombre = i.split()[0]
      edad = int(i.split()[-1])
      if edad > eAprend:
        eAprend = edad
        nAprend = nombre
  print("\nMas longevo")
  print(f"\nNombre: {nAprend} Edad: {eAprend}")
  
  #Este for es un poco mas sencillos, solo verificamos que el ultimo split sea igual a 18, se puede convertir en int, pero de igual forma funcionara en cadena de caracteres.
  print("\nAprendiz con 18")
  for i in lista:
    if i.split()[-1] == "18":
      print(i)

  #Aca se pone que el valor de pre sea pass, para que salte al siguiente proceso, en el cual eliminaremos al instructor de la lista.   
  pre = "pass"
if pre == "pass":
  ins=input("\n\nHay un instructor infiltrado en la lista de aprendices, eliminemoslo,  digita su nombre: ").title()
  print (f"Lo siento {ins} :C")
  #En este for ponemos una variable que recorrera los valores de aprendices, aqui verificamos que el input escrito concuerde con la variable del for, y ambos estan en title para que concuerden, y borraremos el instructor de la lista main que es aprendices, y luego reacomodamos la lista llamada "lista" asi ambas tendran los mismos valores y se podra trabajar con lista mas comodo.
  for nInstru in aprendices:
    if ins in nInstru.title():
      aprendices.remove(nInstru)
      lista=(sorted(aprendices))


  #Aqui se imprime la lista sin el instructor para confirmar que no existe ya
  print("\nLista sin el instructor\n")
  for i, elemento in enumerate(lista):
    print(f"# {i + 1}: {elemento}")

  #Reacomodamos el valor de pre a rank para el siguiente if
  pre ="rank"
if pre == "rank":
  #Aqui se mostraran los primeros 10 aprendices, los del medio y los ultimos por medio de condicionales
  print("\n\nAhora mira los 10 aprendices que estan de primeras, los 10 de la mitad y los 10 ultimos :)")
  print("\nLos 10 primeros:")
  for i, elemento in enumerate(lista):
    if i <= 9:
      print(f"# {i + 1}: {elemento}")
  print("\nLos 10 de la mitad:")
  for i, elemento in enumerate(lista):
    if i > 9 and i <= 19:
      print(f"# {i + 1}: {elemento}")
  print("\nLos 10 ultimos:")
  for i, elemento in enumerate(lista):
    if i > 19:
      print(f"# {i + 1}: {elemento}")


  #Aqui hacemos una nueva variable  para hacer mas procesos 
  nuevoApr="incripted"
  if nuevoApr == "incripted":
     
     #Aqui pedimos el nombre de un aprendiz, la idea es que este de ultimas en la lista
     nombre = input("\n\nIntroduce un aprendiz nuevo :) : ").title()
     edad = int(input("Introduce tu edad {}: ".format(nombre)))

     new=(nombre + " " + str(edad))
     aprendices.insert(-1,new)
     lista=aprendices
     print("\nLista de aprendices\n")
     for i, elemento in enumerate(lista):
      print(f"# {i + 1}: {elemento}") 
#Aqui viene la parte de interactuar con la lista, se puede saltar hasta aqui en la primera pregunta de s/n, este ciclo mantiene en true para hacer varias confirmaciones :)
while True:
  pre2=int(input("\n¿Quieres buscar un valor en la lista? Digite el numero segun lo que buscara:\n1.Nombre o inicial\n2.Estudiantes con cierta edad\n3.Salir\n\nDigite aqui: "))

  #Aqui viene la magia, son 3 opciones, la ultima es para salir del ciclo asi que no tendra un enfoque como tal.
  if pre2 == 1:
    nb = input("\n\nDigite el nombre del aprendiz que desea buscar: ").lower()
    print(f"\nAprendices con el nombre {nb}:\n")
    #En este for verificamos que la palabra digitada o el nombre, concuerde con algo dentro de la lista, asi traera duplicados, iniciales, o que contenga la letra
    for nombreA in lista:
        if nb in nombreA.lower():
            print(f"Aprendiz: {nombreA}")
      
  if pre2 == 2:
    ed=int((input("\n\nDigite la edad de los aprendices que desea buscar: ")))
    print(f"\nLos aprendices con {ed} años son:")
    
    #Este for imprimira todos los que tengan la misma letra dentro del split de la edad, en este si se transformo a entero para que el ejercicio fuera mas acorde
    for i in lista:
      if int(i.split()[-1]) == ed :
        print(i)
  if pre2 == 3:
    break
