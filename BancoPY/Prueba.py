import random

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
    while True:
        cantidad=input("¿De cuánta cantidad deseas hacer el deposito?")
        if cantidad.isdigit():
            break
        else:
            print("Introduce una cantidad en números.")
    while True:
        anos=input("¿A cuántos años deseas hacer el deposito?")
        if anos.isdigit():
            anos=(int)(anos)
            break
        else:
            print("Introduce una cantidad de años en número.")
    comprobarSaldo = ("SELECT saldo FROM cuenta WHERE dni_cliente=%s AND pin=%s")
    valores_comprobarSaldo = (self.dni, self.pin)
    cur.execute(comprobarSaldo, valores_comprobarSaldo)
    data = cur.fetchall()
    removeSaldo = ("UPDATE cuenta SET saldo=(saldo-%s) WHERE dni_cliente=%s AND pin=%s")
    valores_removeSaldo = (cantidad, self.dni, self.pin)
    saldoFloat(data)
    cantidadFloat=float(cantidad)
    if cantidadFloat < data:
        try:
            cur.execute(removeSaldo, valores_removeSaldo)
        except:
            print("Se ha producido un error al retirar del saldo.")
        if anos < 2:
            porcentaje = (round(random.uniform(1.000, 1.010), 3))
        else:
            porcentaje = (round(random.uniform(1.010, 1.020), 3))
        for i in anos:
            cantidadFloat=cantidadFloat * porcentaje
            i+=1
        print("El deposito de ", cantidad," € ha resultado ",cantidadFloat," €")
        addSaldoDeposito = ("UPDATE cuenta SET saldo=(saldo+%s), deposito=(deposito+%s) WHERE dni_cliente=%s AND pin=%s")
        valores_addSaldoDeposito = (cantidadFloat, cantidadFloat, self.dni, self.pin)
        try:
            self.cur.execute(addSaldoDeposito, valores_addSaldoDeposito)
            self.miConexion.commit()
        except:
            print("No se ha podido agregar el valor del deposito al saldo.")
    else:
        print("La cantidad introducida es superior a la del saldo y no se puede hacer el deposito")
def inversion():
    while True:
        cantidad=input("¿De cuánta cantidad deseas hacer la inversion?")
        if cantidad.isdigit():
            break
        else:
            print("Introduce una cantidad en números.")
    while True:
        tipo=input("""Indica el tipo de inversion que deseas hacer:
            1.- Bajo riesgo.
            2.- Alto riesgo.
            3.- Maximo riesgo.""")
        if tipo.isdigit():
            break
        else:
            print("Indica tu selección con números del 1 al 3.")
    comprobarSaldo = ("SELECT saldo FROM cuenta WHERE dni_cliente=%s AND pin=%s")
    valores_comprobarSaldo = (self.dni, self.pin)
    cur.execute(comprobarSaldo, valores_comprobarSaldo)
    data = cur.fetchall()
    removeSaldo = ("UPDATE cuenta SET saldo=(saldo-%s) WHERE dni_cliente=%s AND pin=%s")
    valores_removeSaldo = (cantidad, self.dni, self.pin)
    data=Metodos.saldoFloat(data)
    cantidadFloat=float(cantidad)
    if cantidadFloat < data:
        try:
            self.cur.execute(removeSaldo, valores_removeSaldo)
            miConexion.commit()
        except:
            print("Se ha producido un error al retirar del saldo.")
        if tipo==1:
            porcentaje = (round(random.uniform(-10.0, 10.0), 3))
            cantidadFloat= cantidadFloat*porcentaje
        if tipo==2:
            porcentaje = (round(random.uniform(-50.0, 50.0), 3))
            cantidadFloat = cantidadFloat * porcentaje
        if tipo==3:
            porcentaje = (round(random.uniform(-100.0, 100.0), 3))
            cantidadFloat = cantidadFloat * porcentaje
        print("La inversion de ", cantidad," € ha resultado en ",round(cantidadFloat, 3)," €")
        addSaldoInversion = ("UPDATE cuenta SET saldo=(saldo+%s), inversion=(inversion+%s) WHERE dni_cliente=%s AND pin=%s")
        valores_addSaldoInversion = (cantidadFloat, cantidadFloat, self.dni, self.pin)
        try:
            self.cur.execute(addSaldoInversion, valores_addSaldoInversion)
            miConexion.commit()
        except:
            print("No se ha podido agregar el valor del deposito al saldo.")
    else:
        print("La cantidad introducida es superior a la del saldo y no se puede hacer el deposito")
def saldoFloat(data):
    for num in data:
        numeros=list(num)
        saldoReal=numeros[0]
    return float(saldoReal)
def extraerDinero():
    dni = input("Cual es tu DNI?")
    pin = (int)(input("introduce tu pin"))
    cantidad = (int)(input("Cuanto quieres retirar de tu cuenta?"))
    comprobarSaldo=("SELECT saldo FROM cuenta WHERE dni_cliente=%s AND pin=%s")
    valores_comprobarSaldo=(dni, pin)
    cur.execute(comprobarSaldo, valores_comprobarSaldo)
    data = cur.fetchall()
    removeSaldo=("UPDATE cuenta SET saldo=(saldo-%s) WHERE dni_cliente=%s AND pin=%s")
    valores_removeSaldo=(cantidad, dni, pin)
    addSaldo = ("UPDATE cuenta SET saldo=(saldo+%s) WHERE dni_cliente=%s AND pin=%s")
    valores_addSaldo = (cantidadFloat, dni, pin)
    saldoFloat(data)
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