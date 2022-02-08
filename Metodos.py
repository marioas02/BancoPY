import random

import MySQLdb

from Cliente import Cliente
from Cuenta import Cuenta


def crearCliente_Cuenta():
    # CONEXIÓN CON BD;
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='1234', db='bancopy')
    cur = miConexion.cursor()

    #VARIABLES DEL MÉTODO:

    nuevocliente = Cliente("", "", "", "", "")  # --> Variable para la creación del cliente de tipo "Cliente".
    nuevacuenta = Cuenta("", "", "", "", "")  # --> Variable para la creación de la cuenta, de tipo "Cuenta", del nuevo cliente.

    #QUERYS:
    query_campos_cliente = "INSERT INTO cliente (nombre, primer_apellido, segundo_apellido, dni, contraseña)" \
                          " VALUES (%s, %s, %s, %s, %s)"
    query_campos_cuenta = "INSERT INTO cuenta (dni_cliente, numero_cuenta, pin, saldo, deposito, inversion)" \
                          " VALUES (%s, %s, %s, %s, %s, %s)"
    query_numero_cuenta = "SELECT MAX(numero_cuenta) FROM cuenta"

    #CÓDIGO:
    print()
    print("Empecemos creándo tu perfil de cliente.\nA continuación deberás introducir tus datos personales para darte de alta como cliente.")
    print()
    nuevocliente.nombre = str(input("Tu nombre es:"))
    nuevocliente.primer_apellido = str(input("Tu primer apellido es:"))
    nuevocliente.segundo_apellido = str(input("Tu segundo apellido es:"))

    comp = True
    while comp:
        nuevocliente.dni = input("Número del DNI: ")
        dni_arr = list(nuevocliente.dni)
        if len(nuevocliente.dni) == 9:
            cont = 1
            for i in range(len(nuevocliente.dni)):
                if cont == 9:
                    tablaLetras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D",
                                   10: "X", 11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H",
                                   19: "L", 20: "C", 21: "K", 22: "E"}
                    dni_num = nuevocliente.dni[:-1]
                    letra = tablaLetras[int(dni_num) % 23]
                    if str(dni_arr[i]) == letra:
                        print("DNI correcto.")
                        comp = False
                    else:
                        print("DNI incorrecto.")
                        break
                else:
                    if str(dni_arr[i]).isdigit():
                        cont = cont + 1
                    else:
                        print("DNI incorrecto.")
                        break
        else:
            print("DNI incorrecto.")

    print("Ahora esribe cual quieres que sea tu contraseña de acceso.\n¡IMPORTANTE!: Ten cuidado al escribir con mayúsculas, minúsculas, números etc...")

    while True: # --> Bucle que verifica si la contraseña introducida 2 veces es igual. En caso de que sí, la validamos.
        contraseña1 = str(input("Tu contraseña es: "))
        contraseña2 = str(input("Por seguridad, vuelve a escribir la contraseña: "))
        if (contraseña1 == contraseña2):
            nuevocliente.contraseña = contraseña1
            break
        else:
            print("Las contraseñas introducidas no son iguales. Por favor, escríbelas de nuevo.")

    print()
    print("¡Perfecto! Has sido dad@ de alta como cliente en BancoPY.\nTus datos son:\n-----------------------------")
    print("Nombre: " + nuevocliente.nombre + "\n1ºApellido: " + nuevocliente.primer_apellido + "\n2ºApellido: " + nuevocliente.segundo_apellido + "\nDNI: " + nuevocliente.dni + "\nContraseña: " + nuevocliente.contraseña)
    print("-----------------------------")
    print()

    query_valores_cliente = (nuevocliente.nombre, nuevocliente.primer_apellido, nuevocliente.segundo_apellido, nuevocliente.dni, nuevocliente.contraseña)
    cur.execute(query_campos_cliente, query_valores_cliente)
    miConexion.commit()

    # --------------------------------------------------------------------------------------------------------

    print("Ahora procederemos a abrirte una cuenta 'PY'")
    ultimo_n_cuenta = cur.execute("SELECT numero_cuenta FROM cuenta WHERE id = '1'")
    # nuevacuenta.numero_cuenta = int(ultimo_n_cuenta) + 1

    nuevacuenta.pin = random.randint(1000, 9999) # --> Establecemos un número aleatorio para el PIN del cliente.

    salir = False

    print(ultimo_n_cuenta)
    print(ultimo_n_cuenta+1)
    print(nuevacuenta.numero_cuenta)

    print("¿Deseas abrir esta cuenta con una cantidad de saldo?")
    while not salir:
        abrirconsaldo = int(input("Escribe '0' si no deseas introducir saldo en la cuenta ahora o escribe '1' si deseas introducir saldo."))
        if (abrirconsaldo == 1):
            nuevacuenta.saldo = float(input("¿Qué cantidad deseas ingresar?"))
            print("Perfecto. Tu cuenta ha sido abierta con", nuevacuenta.saldo, "€")
            salir = True
        elif (abrirconsaldo == 0):
            print("Perfecto. Puedes añadir saldo a tu cuenta siempre que quieras.")
            salir = True
        else:
            print("Por favor, escribe uno de los 2 números que se indidan arriba.")


    query_valores_cuenta = (nuevocliente.dni, nuevacuenta.numero_cuenta, nuevacuenta.pin, nuevacuenta.saldo, nuevacuenta.deposito, nuevacuenta.inversion)
    cur.execute(query_campos_cuenta, query_valores_cuenta)
    miConexion.commit()

    miConexion.close()