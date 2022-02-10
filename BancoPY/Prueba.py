conexion=mysql.connector.connect(host='localhost', user='root', passwd='root',deb='banco')
cur=conexion.cursor()
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
    valores_addSaldo=(cantidad, dni, pin)
    try:
        cur.execute(addSaldo, valores_addSaldo)
    except:
        print("Se ha producido un error al añadir el saldo.")
def deposito():
    print("deposito")
def inversion():
    print("inversion")
def saldoInt(data):
    for num in data:
        numeros=list(num)
        saldoReal=numeros[0]
    return int(saldoReal)
def extraerDinero():
    dni = input("Cual es tu DNI?")
    pin = (int)(input("introduce tu pin"))
    cantidad = (int)(input("Cuanto quieres retirar de tu cuenta?"))
    comprobarSaldo=("SELECT saldo FROM cuenta WHERE dni_cliente=%s AND pin=%s")
    valores_comprobarSaldo=(dni, pin)
    cur.execute(comprobarSaldo, valores_comprobarSaldo)
    data = cur.fetchAll()
    removeSaldo=("UPDATE cuenta SET saldo=(saldo-%s) WHERE dni_cliente=%s AND pin=%s")
    valores_removeSaldo=(cantidad, dni, pin)
    saldoInt(data)
    if cantidad < data:
        try:
            cur.execute(removeSaldo, valores_removeSaldo)
        except:
            print("Se ha producido un error al retirar del saldo.")
    else:
        print("La cantidad introducida es superior a la del saldo y no se puede hacer la extracción")
def baja():
    dni=input("Introduce tu DNI?")
    passw=input("Introduce tu contraseña")
    pin=(int)(input("Introduce tu pin"))
    delCuenta=("DELETE FROM cuenta WHERE dni= %s AND pin= %s;")
    valores_delCuenta=(dni, pin)
    delCliente=("DELETE FROM cliente WHERE dni= %s AND contraseña= %s;")
    valores_delCliente=(dni, passw)
    try:
        cur.execute(delCuenta, valores_delCuenta)
        cur.execute(delCliente, valores_delCliente)
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