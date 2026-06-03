# ejercicio 1

#nivel 1
tipo_de_invitacion = input("que tipo de invitacion tienes?").strip().upper()
if tipo_de_invitacion == "VIP":
    print("Bienvenido!")
elif tipo_de_invitacion == "vip":
    print("te falto algo")
else:
    print("acceso denegado")

# nivel 2
edad = int(input("cuantos años tienes?"))
if edad >= 18:
    print("listo! solo una cosa mas...")
else:
    print("acceso denegado")

#nivel 3
codigo_de_seguridad = int(input("tienes codigo de seguridad?"))
if codigo_de_seguridad == 777:
    print("Bienvenido a la fiesta, ya puedes entrar")
else:
    print("acceso denegado")



#ejercicio 2

#nivel 1
nivel_de_estudio = input("cual es tu nivel de estudio?").strip().lower()
if nivel_de_estudio == "universitario":
    print("aprobado")
#nivel 2
años_de_experiencia = float(input("puedes decirnos tus años de experiencia?"))
if años_de_experiencia >= 2.5:
    print("aprobado")
#nivel 3
certificacion_tecnica = input("tienes certificacion tecnica?")
if certificacion_tecnica == "si":
    print("aprobado")
#nivel 4
puntaje_de_prueba = int(input("puedes decirnos tu puntaje de prueba?"))
if puntaje_de_prueba >= 80 and puntaje_de_prueba <= 100:
    print("felicidads, pronto nos contactaremos contigo")
else:
    print("lo sientos, no cumples con los requisitos necesarios")



# ejercicio 3
estatus_cliente = input("cual es tu estatus con nosotros?:").strip().upper()
if estatus_cliente == "SOCIO":
    dia = input("bienvenido socio! nos confirmas que dia es hoy?:").strip().lower()
    if dia == "martes" or dia == "jueves":
        print("felicidades! disfruta tu descuento del 20%")
        metodo_de_pago = input("nos confirmas tu metodo de pago?:").strip().upper()
        if metodo_de_pago == "TARJETA":
            print ("perfecto! tu descuento se apliacara al monto de tu compra")
            monto_de_compra = int(input("cual es el monto de tu compra?:"))
            if monto_de_compra > 500:
                print("felicidades! tu descuento del 20% se ha aplicado")
                descuento = monto_de_compra * 0.80
                print(f"tu monto con descuento es de: {descuento}")
            else:
                print("lo sentimos, tu monto no es valido para el descuento")
        else:
            print ("lo sentimos, el descuento solo aplica para pagos con tarjta")

    else:
        print("lo sentimos, tu descuento solo es valido los dias martes y jueves")
else: 
    print("lo lamento, no cuentas con nuestro beneficio de descuento")


# ejercicio 4
problema = input("el equipo enciende?: ").strip().lower()

if problema == "no":
    pregunta1 = input("El cable de poder está conectado?").strip().lower()
    if pregunta1 == "si":
        pregunta2 = input("El enchufe tiene electricidad?").strip().lower()
        if pregunta2 == "si":
            pregunta3 = input("La fuente hace ruido o gira el ventilador?").strip().lower()
            if pregunta3 == "si":
                pregunta4 = input("Emite algún pitido al intentar encender?").strip().lower()
                if pregunta4 == "si":
                    print("tu equipo presenta una falla, por favor acude a un tecnico")
                else:
                    print("tu equipo presenta fallas leves, por favor realizar chequeo")
            else:
                print("la fuente esta en orden en ese caso")
        else:
            print("por favor verifica el enchufe de electricidad")
    else:
        print("por favor conecta el cable de poder")
else:
    print("tu equipo esta funcionando correctamente")


# ejercicio 5
contrato = input("cual es tu tipo de contrato?").strip().lower()
if contrato == "indefinido":
    ingresos = int(input("monto de tus ingresos:"))
    gastos = int(input("monto de tus gastos: "))
    if ingresos >= gastos:
        ahorros = ingresos- gastos
        if ahorros >= 1000:
            historial_crediticio = input("indica tu historial crediticio:").strip().upper() 
            if historial_crediticio == "BUENO" or historial_crediticio == "EXCELENTE":
                pago_inicial = float(input("indica el porcentaje de tu pago inicial:")) 
                if pago_inicial >= 20.0:
                    fiador = input("cuenta usted con un fiador?").strip().lower()
                    if fiador == "si" or ahorros >= 2000:
                        print("credito asignado!")
                    else:
                        print("es necesario un fiador o ahorros mayores a 2000")
                else:
                    print("su pago inicial no cumple con lo establecido")
            else:
                print("su historial crediticio no cumple con lo establecido")
        else:
            print("sus ahorros no cumplen con lo establecido")
    else:
        print("sus ingresos no cumplen con lo establecido")
else:
    print("tu contrato ya es definido")
