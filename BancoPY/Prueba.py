conexion=mysql.connector.connect(host='localhost', user='root', passwd='root',deb='banco')
query=conexion.cursor()
def alta():
    print("Alta")
def cambiarPin():
    print("cambiar pin")
def detalles():
    print("mostrar detalles")
def agregarSaldo():
    dni = input("Cual es tu DNI?")
    pin = (int)(input("introduce tu pin"))
    cantidad=(int)(input("Cuanto quieres ingresar en tu cuenta?"))
    addSaldo=("UPDATE cuenta SET saldo=(saldo+%s) WHERE dni_cliente=%s AND pin=%s")
    try:
        query.execute(addSaldo, cantidad, dni, pin)
    except:
        print("Se ha producido un error al añadir el saldo.")
def deposito():
    print("deposito")
def inversion():
    print("inversion")
def extraerDinero():
    dni = input("Cual es tu DNI?")
    pin = (int)(input("introduce tu pin"))
    cantidad = (int)(input("Cuanto quieres retirar de tu cuenta?"))
    comprobarSaldo=("SELECT saldo FROM cuenta WHERE dni_cliente=%s AND pin=%s")
    removeSaldo=("UPDATE cuenta SET saldo=(saldo-%s) WHERE dni_cliente=%s AND pin=%s")
    if cantidad>query.execute(comprobarSaldo, cantidad, dni, pin):
        try:
            query.execute(removeSaldo, cantidad, dni, pin)
        except:
            print("Se ha producido un error al retirar del saldo.")
    else:
        print("La cantidad introducida es superior a la del saldo y no se puede hacer la extracción")
def baja():
    dni=input("Cual es tu DNI?")
    passw=input("Introduce tu contraseña")
    pin=(int)(input("introduce tu pin"))
    delCuenta=("DELETE FROM cuenta WHERE dni= %s AND pin= %s")
    delCliente=("DELETE FROM cliente WHERE dni= %s AND contraseña= %s")
    try:
        query.execute(delCuenta, dni, pin)
        query.execute(delCliente, dni, passw)
    except:
        print("No se ha podido eliminar la cuenta")


opcion=(int)(input("""Seleciona una opcion:
1.- Dar de alta.
2.- Iniciar sesion"""))
if opcion==1:
    alta()
elif opcion==2:
    opcion = (int)(input("""Seleciona una opcion:
    1.- Cambiar pin.
    2.- Ver detalles.
    3.- Añadir saldo.
    4.- Hacer deposito
    5.- Hacer inversion
    6.- Sacar dinero
    7.- Baja"""))
    if opcion==1:
        cambiarPin()
    elif opcion==2:
        detalles()
    elif opcion==3:
        agregarSaldo()
    elif opcion==4:
        deposito()
    elif opcion==5:
        inversion()
    elif opcion==6:
        extraerDinero()
    elif opcion==7:
        baja()
    else:
        print("Selecciona una opción valida")
else:
    print("Opcion no valida")