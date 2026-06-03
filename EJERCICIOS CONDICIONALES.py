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

