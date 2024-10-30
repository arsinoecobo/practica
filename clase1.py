print("Bienvenido a su calculadora")
print("Seleccione la operacion que desea realizar")
print("1 suma")
print("1 resta")
print("1 multiplicacion")
print("1 division")
#RECEPCION DE LA SELECCION DEL USUARIO
eleccion = input ("<ingrese el numero de la operacion que desea realizar (1-2-3-4):")
#VALIDAR DESICION DEL USUARIO
if eleccion not in ["1","2","3","4"]:
    print("Opcion invalida , Selecciona una opcionn valida")
    exit()
#Solicitar los numeros al usuario
try:
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("Ingrese el segundo numero:"))
except ValueError:
    print("Entrada invalida, Ingrese un numero valido")  
    exit()
    #REALIZAR LA OPERACION SELECCIONADA
if eleccion == "1":
    resultado = num1+num2
    operacion = "suma" 

if eleccion == "2":
    resultado = num1-num2
    operacion = "resta"  

if eleccion == "3":
    resultado = num1*num2
    operacion = "multiplicacion"     

if eleccion == "4":
    resultado = num1/num2
    operacion = "division" 
#MOSTRAR EL RESULTADO TOTAL
print(f"El resultado {operacion} entre {num1} y {num2} es: {resultado}")