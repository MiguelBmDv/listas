import time
aprendices = {}
for i in range(3):
    nombre = input("Introduce un nombre: ").upper()
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices[nombre] = edad
    if i == 2:
      nombre = input("Introduce el nombre del tu instructor: ").upper()
      edad = input(f"Introduce la edad de {nombre}: ")
      instru = {nombre: edad, **aprendices} 
      aprendices = instru
      break

ordAprendiz= dict(sorted(aprendices.items()))
print("\nLista de aprendices\n")
for i, (nombre, edad) in enumerate(aprendices.items()):
    print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
pre=(input("\nQuieres ver cuantos aprendices tienen 18 y cual es el mas longevo? s/n: " ).lower())
if pre == "s":
  print("\nAprendiz mas longevo:")
  print(max(aprendices, key=aprendices.post))
  print("\nAprendices con 18 años:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if edad == "18":
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  pre = "password"
if pre == "pass":
  ins=input("\n\nHay un instructor infiltrado en la lista de aprendices, eliminemoslo,  digita su nombre: ").upper()
  print (f"Lo siento {ins} :C")
  del aprendices[ins]
  del ordAprendiz[ins]
  print("\nLista sin el instructor\n")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  time.sleep(5)
  pre ="rank"
  time.sleep(5)
if pre == "rank":
  print("\n\nAhora mira los 10 aprendices que estan de primeras, los 10 de la mitad y los 10 ultimos :)")
  print("\nLos 10 primeros:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i <= 9:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  print("\nLos 10 de la mitad:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i >= 9 and i <= 19:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
    else:
      print("No hay suficientes aprendices")
  print("\nLos 10 ultimos:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i >= 19:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
    else:
      print("No hay suficientes aprendices")
  nombre="incripted"
  if nombre == "incripted":
     nombre = input("\n\nIntroduce un nombre para agregar de ultimas :) : ").upper()
     edad = int(input("Introduce tu edad {}: ".format(nombre)))
     aprendices[nombre] = edad
     ordAprendiz= dict(sorted(aprendices.items()))
     print("\nLista de aprendices\n")
     for i, (nombre, edad) in enumerate(aprendices.items()):
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")   
while True:
  time.sleep(2)
  pre2=(input("\n¿Quieres buscar un valor en la lista? Digite el numero segun lo que buscara:\n1.Nombre o que contenga x letra\n2.Estudiantes con cierta edad\n3.Salir\n\nDigite aqui: "))
  if pre2 == 1:
    nb = input("\n\nDigite el nombre del aprendiz que desea buscar: ").upper()
    print(f"\nAprendices con el nombre {nb}:")
    for nombre, edad in ordAprendiz.items():
        if nb in nombre.upper():
            print(f"Nombre: {nombre}, Edad: {edad}")
  if pre2 == 2:
    ed=int((input("\n\nDigite la edad de los aprendices que desea buscar: ")))
    print(f"\nLos aprendices con {ed} años son:")
    for i, (nombre, edad) in enumerate(ordAprendiz.items()):
      if edad == ed:
        print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")

  if pre2 == 3:
    break