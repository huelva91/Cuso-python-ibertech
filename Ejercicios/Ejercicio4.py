aula_1 = []
aula_2 = []
aula_3 = []
colegio = [aula_1, aula_2, aula_3]
alumnos = []
opcion = 0
while (not opcion == 5):
    print("1. Insertar alumno")
    print("2. Mostrar alunmnos colegio")
    print("3. Mostrar alumnos aula")
    print("4. Buscar alunmo")
    print("5. Salir")

    opcion = int(input("\nSeleccione una opcion"))

    if opcion == 1:
        # En que aula quieres meter al alumno (1,2,3) --> DNI, Nombre, Apellidos
        print("Insertar alumno ")
        aula = int(input("Introduzca el aula donde quiere anadir al alumno"))
        dni = input("Inserta el DNI del alumno")
        nombre = input("Inserta el nombre del alumno")
        apellidos = input("Inserta el apellidos del alumno")
        alumno = {"DNI": dni, "Nombre": nombre, "Apellidos": apellidos}
        alumnos.append(alumno)
        if aula == 1:
            aula_1.append(alumno)
        elif aula == 2:
            aula_2.append(alumno)
        elif aula == 3:
            aula_3.append(alumno)
        else:
            print("Debes introducir un aula correcta")

        print(alumnos[0])

    elif opcion == 2:
        # Todos los alumnos del colegio por aula.
        print("Mostrar alunmnos colegio ")
        for alumno_lista in alumnos:
            print(alumno_lista)
    elif opcion == 3:
        # De que aula quiere mostrar los alumnos (1,2,3)
        aula = int(
            input("Introduzca el aula de donde quiere mostrar los alumnos"))
        print("Mostrar alumnos aula ")
        if aula == 1:
            for alumno_aula in aula_1:
                print(alumno_lista)
        elif aula == 2:
            for alumno_aula in aula_2:
                print(alumno_lista)
        elif aula == 3:
            for alumno_aula in aula_3:
                print(alumno_lista)
        else:
            print("Debes introducir un aula correcta")
    elif opcion == 4:
        # En que aula se encuentra el alumno ese DNI
        print("Buscar alunmo")
    elif opcion == 5:
        print("Adios")
    else:
        print("Opcion incorrecta, vuelve a intentarlo")
