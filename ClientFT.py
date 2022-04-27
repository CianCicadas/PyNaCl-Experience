import socket
IP = socket.gethostbyname(socket.gethostname())
Puerto = 4456
Dir = (IP, Puerto)
Formato = "utf-8"
Tamanio = 1024

def main():
    # solo envia, no comprueba nada

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(Dir)

    archivo = open("ArchivoMuestra.txt")
    datos = archivo.read()

    client.send("Archivo.txt".encode(Formato))
    msj = client.recv(Tamanio).decode(Formato)
    print(f"[Server]: {msj}")

    client.send(datos.encode(Formato))
    msjAlt = client.recv(Tamanio).decode(Formato)
    print(f"[Server]: {msjAlt}")

    archivo.close()
    client.close()

if __name__ == "__main__":
    main()
