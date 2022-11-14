lista_emails = ["hola@gmail.com", "a dios.com", "mal@@.com", "asadfa.eeeeeee"]

for email in lista_emails:
    email = email.strip()
    errores = ""
    if email.count(" ") > 0:
        errores += "No puede haber espacios en blanco"
    if not email.count("@")==1:
        errores+= "Debe haber un @ "
    if email.split("@")[-1].count(".") >+ 1:
        errores+= "Despues de la arroba tiene que haber un ."
    if not email[ email.find("@") + 1 : ].find(".") > 1:
        errores+= "La distancia entre el @ y el primer punto despues de la arroba debe ser mayor de 2"
    if len(email.split(".")[-1]) < 2 or len(email.split(".")[-1]) > 5:
        errores+= "El subdominio del email debe estar entre 2 y 5"

    if errores == "":
        print("El email " + email + " es correcto")
    else:
         print("El email " + email + " no es correcto " + errores)
