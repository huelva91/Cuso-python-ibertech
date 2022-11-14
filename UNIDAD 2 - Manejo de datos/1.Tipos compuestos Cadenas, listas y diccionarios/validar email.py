
#Despues de la @ tiene que haber al menos un punto
#La distancia entre la @ y el punto tiene que ser al menos de 2 caracteres
#despues del ultimo punto tiene que haber alg menos entre 2 y 5 caracteres

correos = ["hola@gmail.com", "a dios.com", "mal@@   .com", "asadfa.eeeeeee"]

for correo in correos:
    if " " in correo:
        print("Hay espacios en el correo {}".format(correo))
    if not "@" in correo:
        print("Este correo no contiene @: {}".format(correo))
    if len(correo.split("@")[1:-1]) < 2:
        print("La distancia entre el @ y el punto tiene que ser al menos de 2 caracteres: {}".format(correo))

        print("despues del ultimo punto tiene que haber alg menos entre 2 y 5 caracteres")



