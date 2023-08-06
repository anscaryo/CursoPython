def divide():
    while True:    
        try:
            num1 = float(input("Introduce el primer numero: "))
            num2 = float(input("Introduce el segundo numero: "))
            print(f"La división es: {num1/num2}")
            break
        except ZeroDivisionError:
            print("No se puede dividir por 0")

        except ValueError:
            print( "Valor erroneo.")
            
        finally:
            print("Cálculo realizado.")

    print("Esta linea se ejecuta al final del \"try\"")

    
divide()
