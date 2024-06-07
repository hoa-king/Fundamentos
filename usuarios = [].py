usuarios = []
contrasena = []
while True:
    try:


        print("Elija una opción entre 1 y 4")
        print("1. Inicio de sesión")
        print("2. Registrar usuario")
        print("3. Elimianr usuario")
        print("4. Salir")
        resp = int(input("Presione la acción que desea ejecutar: "))
        if resp == 1:
            if not usuarios:
                print ("No hay usuarios registrados")
                print("Debe ir al menú 2 y registrar un usuario.")
            if len(usuarios)> 0:
                print("Inicio de sesión existoso")
        elif resp == 2:
            while True:
                try:
                    nuevo_usuario = input("Ingrese nombre de nuevo usuario: ")
                    usuarios.append(nuevo_usuario)
                    nueva_contrasena = input("Ingrese nueva constraseña: ")
                    contrasena.append(nueva_contrasena)
                    respuesta = int(input("Desea agregar nuevo usuario? si=1/no=2: "))
                    if respuesta == 2:
                        break
                except:
                    print("Operación no válida")
        elif resp == 3:
            usuario_borrar = input("Escriba el nombre de usuario que desa borrar: ")
            usuarios.remove(usuario_borrar)
            print("Usuario borrado exitosamente")
        elif resp == 4:
            print("saliendo...")
            break
    except ValueError:
        print("Operación incorrecta, vuelva a intentarlo")
