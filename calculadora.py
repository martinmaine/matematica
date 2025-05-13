print("Calculadora de números binarios ¿Qué cálculo desea hacer?")
while True: 
    print("1. Convertir números decimales en binarios")
    print("2. Convertir números binarios en decimales")
    
    opcion = input("Elija una opción (1 o 2): ")
    
    if opcion == "1":
        # Decimal a binario
        entrada = input("Ingrese el número decimal que quiere convertir en binario: ")
        
        # Validación  1
        es_valido = True
        for caracter in entrada:
            if caracter not in "0123456789":
                es_valido = False
                break
        
        if es_valido and entrada != "":
            numero_decimal = int(entrada)
            
            # Algoritmo de conversión de decimal a binario
            if numero_decimal == 0:
                resultado = "0"
            else:
                resultado = ""
                numero_temp = numero_decimal
                
                while numero_temp > 0:
                    residuo = numero_temp % 2
                    resultado = str(residuo) + resultado
                    numero_temp = numero_temp // 2
                    
            print(f"El número decimal {numero_decimal} son {resultado} en binario.")
            break  # Sale del bucle principal después de completar la conversión
        else:
            print("Error: Debe ingresar un número decimal válido.")
            # Vuelve al inicio del bucle principal
    
    elif opcion == "2":
        # Conversión de binario a decimal
        numero_binario = input("Ingrese el número binario que quiere convertir en decimal: ")
        
        # Validación 2
        es_binario_valido = True
        for bit in numero_binario:
            if bit not in "01":
                es_binario_valido = False
                break
        
        if es_binario_valido and numero_binario != "":
            decimal = 0
            posicion = 0
            for bit in reversed(numero_binario):
                if bit == '1':
                    decimal += 2 ** posicion
                posicion += 1
                
            print(f"El número binario {numero_binario} son {decimal} en decimal.")
            break  # Sale del bucle principal después de completar la conversión
        else:
            print("Error: Debe ingresar un número binario válido (compuesto solo de 0 y 1).")
            # Volvemos al inicio del bucle principal
            
    else:
        print("Opción no válida. Por favor, elija 1 o 2.")
        # Volvemos al inicio del bucle principal
