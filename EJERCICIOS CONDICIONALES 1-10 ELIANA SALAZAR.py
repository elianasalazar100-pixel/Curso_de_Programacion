# ejercicio 1
distancia = input("Indicanos por favor tu distancia:").strip().lower()
if distancia <= "20 km":
    cliente = input("¿Eres cliente prime o estandar?: ").strip().lower()
    if cliente == "prime":
        print("perfecto! eres apto para un envio rapido")
    if cliente == "estandar":
        print ("perfecto, eres apto para un envio estandar")
else:
    print("Lo sentimos, no contamos con entregas a esa distancia")

# ejercicio 2
usuario = input("indica nombre de usuario:").strip().lower()
if usuario == "admin":
    contraseña = input("indica tu contraseña:").strip().lower()
    if contraseña == "12345":
        print("bienvenido admin, has iniciado sesion.")
    else:
        print("contraseña invalida")
else:
    print("usuario invalido.")

# ejercicio 3
promedio = int(input("Indica tu promedio de notas:"))
if promedio >= 8.5 or promedio <= 10:
    ingreso = int(input("Indica tu ingreso familiar:"))
    if ingreso < 1500:
        print("eres apto para la beca!")
    if ingreso >= 1500:
        print("tus ingresos son mayores a lo estipulado en nuestros parametros")
else:
    print("lo sentimos, tu promedio no es apto para una beca.")

# ejercicio 4
edad = int(input("Indicanos tu edad:"))
if edad <= 12:
    print("Tu descuento es del 50%")
elif edad > 12 and edad <= 17:
    print("eres estudiante?:")
    estudiante = input("responde si o no:").strip().lower()
    if estudiante == "si":
        print("Tu descuento es del 30%")
    elif input("Cuentas con un pase vip?:").strip().lower() == "si":
        print("Tu descuento es del 10%")
    else:
        print("No tienes descuento disponible, disculpa.")

# ejercicio 5
salario = int(input("Ingresa la cantidad de tu salario:"))
if salario > 1000:
    print("indicanos tu puntaje de credito:")
    puntaje = int(input())
    if puntaje > 600:
        print("cuentas con alguna deuda pendiente?")
        deuda = input().strip().lower()
        if deuda == "si":
            print("Lo lamento, cuentas con deudas por saldar")
        else:
            print("felicidades! prestamos asignado.")
    else:
        print("lo lamento, tu puntaje es insuficiente para aspirar al prestamo")
else:
    print("lo lamento, tu salario no es suficiente para aspirar al prestamo")


# ejercicio 6
destino = input("tu destino de viaje es nacional o internacional?:").strip().lower()
if destino == "nacional":
    peso = input("indicanos el peso de tu equipaje:").strip().lower()
    if peso > "5kg":
        print("tu equipaje incluira un costo extra ya que excede el peso permitido,")
    else:
        print("tu equipaje cumple con el peso permitidio, no se aplicara cargos extras.")
if destino == "internacional":
    continente = input("indicanos a que continente te diriges:").strip().lower()
    if continente == "europa":
        print("perfecto, tu equipaje se enviara por via maritima.")
    elif continente == "asia":
        print("perfecto, tu equipaje se enviara por via aerea.")
    else:
        print("lo sentimos, las tarifas de equipaje no aplican para el continente indicado.")
else:print("error.")


# ejercicio 7
metas = input("haz cumplido con las metas establecidas para este mes?:").strip().lower()
if metas == "si":
    print("perfecto, indica tu puntualidad:")
    puntualidad = int(input("puntualidad: "))
    if puntualidad > 90:
        print("felicidades, has pasado la evaluacion laboral.")
elif metas == "no":
    print("indica cantidad de asistencias a las capacitaciones:")
    asistencias = int(input("asistencias: "))
    if asistencias > 3:
        print("felicidades, has pasado la evaluacion laboral.")
    else:
        print("evaluacion laboral reprobada.")
else:
    print("respuesta no valida, por favor responde con 'si' o 'no'.")


#ejercicio 8
a = int(input("ingrese un primer valor: "))
b = int(input("ingrese un segundo valor: "))
c = int(input("ingrese un tercer valor: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    print ("datos no validos")
elif a == b == c:
    print("el triangulo es equilatero")
elif a == b or a == c or b == c:
    print("el triangulo es isoceles")
else:
    print("el triangulo es escaleno")


# ejercicio 9 
ingresos = int((input("indica el monto de tus ingresos:")))
if ingresos >= 20000 and ingresos <= 50000:
    dependientes = int(input("indique la cantidad de dependientes a su cargo:"))
    if dependientes > 3:
        print("aprobado para subsidio.")
elif ingresos > 50000:
    estado_civil = input("indicanos tu estado civil:").strip().lower()
    if estado_civil == "casado":
        dependientes = int(input("indique la cantidad de dependientes a su cargo:"))
    if dependientes > 2:
        print("aprobado para subsidio.")
    elif estado_civil == "soltero":
        dependientes = int(input("indique la cantidad de dependientes a su cargo:"))
        if dependientes < 2:
            print("subsidio no aprobado.")
    else:
        print("estado civil no valido.")
else:
    print("ingresos no validos.")



# ejercicio 10
espada = 80
armadura = 50
magia = 95
mana = 100
escudo = 70

ataque = input("¿Deseas atacar con espada o magia?:").strip().lower()
if ataque == "espada":
    print(f"realizaste un ataque con espada, tu daño fue de {espada - armadura}%")
elif ataque == "magia":
    print(f"realizaste un ataque con magia, tu daño fue de {magia - mana}%")
else:
    defensa = input("¿Deseas defenderte con escudo?:").strip().lower()
    if defensa == "si":
        print(f"te defendiste con escudo, tu defensa fue de {escudo}%")
    elif defensa == "no":
        print("no te defendiste, el enemigo te atacara sin resistencia.")
    else:
        print("respuesta no valida")