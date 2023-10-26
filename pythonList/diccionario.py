#Este ejercicio es el mismo solo que se trabaja con diccionarios, lo realice por la simple de manejar, es mas facil ya que se esta manejando una clave y valor, algo que nos ahorra el hecho de buscar sentencias o funciones adicionales para separar cadenas de caracteres, aproveche el recurso de clave y valor para convertir el nombre en clave y la edad en valor :)

#Hay algo que depronto no esta bien para el ejercicio y es que los diccionarios no manejan orden, por ende tuve que ingeniarmelas para hacer ciertos puntos

#Se crea un diccionario vacio
aprendices = {}

# Se crea un ciclo for, el cual tiene un rango de 30, este ciclo registrara los datos del estudiante, y al llegar al registro 30(29) directamente preguntara por el instructor y se registrara en la lista, estos tienen el .title para tener la primera mayuscula, y los valores estan concatenados en un string para que queden como un solo elemento en la lista
for i in range(30):
    nombre = input("Introduce un nombre: ").upper()
    edad = int(input(f"Introduce la edad de {nombre}: "))
    aprendices[nombre] = edad
    if i == 29:
      nombre = input("Introduce el nombre del tu instructor: ").upper()
      edad = int(input(f"Introduce la edad de {nombre}: "))
      instru = {nombre: edad, **aprendices} 
      #Esto es algo adicional, como los diccionarios no manejan orden, cree una variable que manejara la clave y valor del instructor, y le agrego despues de eso toda la informacion del dic aprendices, por eso los **, para que la agregue al final, y asi el isntructor estara en la posicion inicial.

      aprendices = instru
      break
#En este paso manejo una lista que la reconvierto en diccionario, me explico, el diccionario actual con sus claves y valores, los paso a una lista ordenada, perooo sigue teniendo su estructura de diccionario porque se vuelve a convertir
ordAprendiz= dict(sorted(aprendices.items()))

print("\nLista de aprendices\n")
#Aqui se sigue usando el dic de aprendices para no dañar el ejemplo de que este en posicion inicial.
for i, (nombre, edad) in enumerate(aprendices.items()):
    print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  
pre=(input("\nQuieres ver cuantos aprendices tienen 18 y cual es el mas longevo? s/n: " ).lower())
if pre == "s":
  print("\nAprendiz mas longevo:")

  #Aqui explicare algo que se vera en partes del documento y seria bueno entenderlo :)
  #max lo usare para comparar en este caso la edad maxima, pero esto solo se podra por medio del key y el get
  #El key acompaña al max, ya que es lo que tomara de referencia de comparacion, es decir a partir de lo que este al lado del = sera el elemento a comparar, y se pone aprendices.get porque lo que usara seran los valores asociados a las claves de aprendices :)
  print(max(aprendices, key=aprendices.get))

  print("\nAprendices con 18 años:")
  #Aqui a destacar es algo que esta en casi todos los for, y es el .item, basicamente al igual que el .get, lo que quiero aqui es asociar claves y valores, entonces nombre sera la clave del diccionario "ordenado" y el item es el valor de esa clave
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if edad == 18:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
      #Aca se pone que el valor de pre sea pass, para que salte al siguiente proceso, en el cual eliminaremos al instructor del diccionario.   
  pre = "pass"
if pre == "pass":
  ins=input("\n\nHay un instructor infiltrado en la lista de aprendices, eliminemoslo,  digita su nombre: ").upper()
  print (f"Lo siento {ins} :C")
  #Para diccionarios no sirve el remove, asi que usamos el del para eliminar claves y valores
  del aprendices[ins]
  del ordAprendiz[ins]

  #lista que confirma su inexistencia en la lista
  print("\nLista sin el instructor\n")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")

  #Reacomodamos el valor de pre a rank para el siguiente if
  pre ="rank"
if pre == "rank":
  print("\n\nAhora mira los 10 aprendices que estan de primeras, los 10 de la mitad y los 10 ultimos :)")
  #Nada distinto a lo anterior, solo son for que muestren ciertos aprendices bajo sus condiciones.
  print("\nLos 10 primeros:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i <= 9:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  print("\nLos 10 de la mitad:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i >= 9 and i <= 19:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  print("\nLos 10 ultimos:")
  for i, (nombre, edad) in enumerate(ordAprendiz.items()):
    if i >= 19:
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}")
  
   #Aqui hacemos una nueva variable  para hacer mas procesos 
  nombre="incripted"
  if nombre == "incripted":
     nombre = input("\n\nIntroduce un nombre para agregar de ultimas :) : ").upper()
     edad = int(input("Introduce tu edad {}: ".format(nombre)))
      #Aqui se agrega el aprendiz y directamente estara de ultimas, ya que no se maneja orden, y volvemos a acomodar el diccionario ordenado para mas procesos
     aprendices[nombre] = edad
     ordAprendiz= dict(sorted(aprendices.items()))
     print("\nLista de aprendices\n")
     for i, (nombre, edad) in enumerate(aprendices.items()):
      print(f"# {i + 1}: Nombre: {nombre}, Edad: {edad}") 

#Aqui viene la parte de interactuar el diccionario, se puede saltar hasta aqui en la primera pregunta de s/n, este ciclo mantiene en true para hacer varias confirmaciones :)   
while True:
  pre2=int(input("\n¿Quieres buscar un valor en la lista? Digite el numero segun lo que buscara:\n1.Nombre o que contenga x letra\n2.Estudiantes con cierta edad\n3.Salir\n\nDigite aqui: "))

  #Estos 3 condicionales son faciles de entender por el manejo del diccionario, aqui solo compara claves y valores, a diferencia de las listas que era con el split
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
  #Sale del ciclo
  if pre2 == 3:
    break
