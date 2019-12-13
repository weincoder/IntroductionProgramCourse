#en este código podremos ver como capturar entradas del teclado

print(input("hola por favor ingrese su nombre : "))

#para el caso anterior obtenemos la entrada del usuario empleando la función input
#en este caso se mostrará en pantalla el nombre ingresado por la persona

#Todas las entradas se toman coman String por la tanto deben ser convertidas int, float
#en caso de requerirlo

edad = int(input("ingrese su edad : "))
estatura = float(input("ingrese su estatura : "))
nombre = input ("ingrese su nombre : ")

print( "hola" , nombre ,"su edad es ", edad , "su estatura" , estatura)

#Con esto podríamos hacer preguntas para casos prácticos por ejemplo
#Deseamos saber si el cliente tiene suficiente dinero para comprar un computador
# de 2000 dolares

dinero = float ( input ("ingrese por favor cuanto dinero usted posee en dolares : "))

if ( dinero > 2000 ):
    print ("Afortunadamente tiene suficiente dinero para comprar el pc y le sobra", dinero -2000)
elif ( dinero < 2000 ):
    print ( "le falta dinero a saber", dinero -2000)
    decision = int (
                   input ("""
                   le ofrecemos un credito al 2 porciento 
                   de interes mensual para que haga uso de el ingrese 
                   1. Aprobar 
                   2. no acceder al credito
                   su decesion : """))
    if (decision == 1):
        print ("usted a accedido al credito y le daremos su computador, por lo tanto tiene una deuda de",2000-dinero,"dolares con un interes del 2% anual")
    else: print ("Gracias lo esperamos pronto")
else: print("tiene justo lo necesario muchas gracias ya le daremos el pc")
   
