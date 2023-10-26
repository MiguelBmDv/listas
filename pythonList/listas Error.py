import time
#Los errores se presentan en posicionamientos, y en como se representan los valores escritos
aprendices = []
for i in range(3):
    nombre = input("Introduce un nombre: ").title()
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices.append(nombre + " " + str(edad))
    if i == 2: 
      nombre = input("Introduce el nombre del tu instructor: ").title()
      edad = int(input(f"Introduce la edad de {nombre}: "))
      instru = (nombre + " " + str(edad))
      aprendices.insert(1,instru) 
      break

print("\nLista de aprendices\n")
for i, elemento in enumerate(aprendices):
    print(f"# {i + 1}: {elemento}")    
lista=(sorted(aprendices))
pre=(input("\nQuieres ver cuantos aprendices tienen 18 y cual es el mas longevo? s/n: " ).lower())

if pre == "s":
  nAprend = None
  eAprend= 0
  for i in lista:
      nombre = i.split()[0]
      edad = int(i.split()[1])
      if edad > eAprend:
        eAprend = edad
        nAprend = nombre
  print("\nMas longevo")
  print(f"\nNombre: {nAprend} Edad: {eAprend}")
  print("\nAprendices con 18")
  for i in lista:
    if i.split()[1] == "18":
      print(i) 
  pre = "pass"
if pre == "pass":
  ins=input("\n\nHay un instructor infiltrado en la lista de aprendices, eliminemoslo,  digita su nombre: ").title()
  print (f"Lo siento {ins} :C")
  for nInstru in aprendices:
    if ins in nInstru.upper():
      aprendices.remove(nInstru)
      lista=(sorted(aprendices))
  print("\nLista sin el instructor\n")
  for i, elemento in enumerate(lista):
    print(f"# {i + 1}: {elemento}")
  time.sleep(5)
  pre ="rank"
  time.sleep(5)
if pre == "rank":
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
  nuevoApr="incripted"
  if nuevoApr == "incripted":
     nombre = input("\n\nIntroduce un aprendiz nuevo :) : ").title()
     edad = int(input("Introduce tu edad {}: ".format(nombre)))
     new=(nombre + " " + str(edad))
     aprendices.insert(-1,new)
     lista=aprendices
     print("\nLista de aprendices\n")
     for i, elemento in enumerate(lista):
      print(f"# {i + 1}: {elemento}") 
while True:
  time.sleep(2)
  pre2=int(input("\n¿Quieres buscar un valor en la lista? Digite el numero segun lo que buscara:\n1.Nombre o inicial\n2.Estudiantes con cierta edad\n3.Salir\n\nDigite aqui: "))
  if pre2 == 1:
    nb = input("\n\nDigite el nombre del aprendiz que desea buscar: ").lower()
    print(f"\nAprendices con el nombre {nb}:\n")
    for nombreA in lista:
        if nb in nombreA.lower():
            print(f"Aprendiz: {nombreA}")    
  if pre2 == 2:
    ed=int((input("\n\nDigite la edad de los aprendices que desea buscar: ")))
    print(f"\nLos aprendices con {ed} años son:")
    for i in lista:
      if float(i.split()[1]) == ed :
        print(i)
  if pre2 == 3:
    break