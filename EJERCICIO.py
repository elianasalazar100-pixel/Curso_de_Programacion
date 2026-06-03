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
