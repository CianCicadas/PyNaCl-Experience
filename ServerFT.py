import socket
import nacl
import nacl.utils
import nacl.secret
import nacl.pwhash

IP = socket.gethostbyname(socket.gethostname())
Puerto = 4456
Dir = (IP, Puerto)
Formato = "utf-8"
Tamanio = 1024

def cifrar(nArchivo, llave):
    archivoSC = open(nArchivo, "rb")
    datosSC = archivoSC.read()
    archivoSC.close()

    cont = nacl.secret.SecretBox(llave)
    datosCC = cont.encrypt(datosSC)

    archivoCC = open("CC-"+nArchivo, "wb")
    archivoCC.write(datosCC)
    archivoCC.close()

def main():
    # solo envia, no comprueba nada
    print("[Inicializando...]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(Dir)
    server.listen()
    print("[Escuchando...]")

    while True:
        conx, dir = server.accept()
        print(f"[Nueva conexion] {dir} conectado")

        nArchivo = conx.recv(Tamanio).decode(Formato)
        print(f"[Recibido] {nArchivo} recibido")
        archivo = open(nArchivo, "w")
        conx.send("Nombre de archivo recibido".encode(Formato))

        datos = conx.recv(Tamanio).decode(Formato)
        print(f"[Recibido] Datos recibidos")
        archivo.write(datos)
        conx.send("Datos recibidos".encode(Formato))
        archivo.close()
        conx.close()
        print(f"[Desconectado] {dir} conexion terminada")


        kdf = nacl.pwhash.argon2i.kdf
        salt = nacl.utils.random(16)
        password = "EntregaCifrada".encode(Formato)
        llave = kdf(nacl.secret.SecretBox.KEY_SIZE, password,salt)
        cifrar(nArchivo, llave)

if __name__ == "__main__":
    main()
