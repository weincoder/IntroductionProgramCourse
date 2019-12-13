#En este caso explicaremos el ciclo while
#Este ciclo se ejecutará mientras una condición sea cierta
#Cuando deje de serlo se saldrá de el

#--------Ejemplo 1 ------#

#ahorremos hasta tenere suficiente para el computador


dinero = float ( input ( "ingrese el dinero que tiene en este momento ahorrado para el computador : "))
precio = float ( input ( "ingrese el valor del computador deseado : "))

if dinero >= precio : print ("tenemos lo necesario")

#en caso de que tengamos suficiente dinero jamás ingresará por esta opción
while (precio > dinero) :
    print("necesitamos ahorar, ahorremos en uno en uno")
    dinero += 1
    print( "usted posee", dinero, "le falta", precio - dinero, "para completar su objetivo")

print ("fin del ejemplo 1")


#--------Ejemplo 2 ------#

#En este caso podremos ver como emplear el while negado

#tratemos que alguien adivine un numero del 1 al 10 

numero_a_adivinar = 3

numero_elejido = int ( input ("ingrese un número del 1 al 10 : "))

mensaje_de_consolacion = """sigue intentando aun puedes por favor ingresa un numero 
                            del 1 al 10 hasta que adivines el numero secreto """

while not (numero_a_adivinar == numero_elejido) :
    numero_elejido = int (input  (mensaje_de_consolacion))

print ("fin segundo ejemplo dos")



#--------Ejemplo 3 ------#

#Al menos menciona una letra de la palabra misteriosa!!!

#Constantes

mensaje_inicial = "bienvenido trata de acertar al menos una letra de nuestra palabra misteriosa"
mensaje_pregunta = "¿podrás lograrlo? \n ingresa una letra :  "
palabra_secreta = "python"
mensaje_consolacion = "vamos tu puedes !"
mensaje_victoria = "felicidades acertaste la letra la palabra es {}"


#-----------------------------------------------#
print (mensaje_inicial)
#variables de entrada
letra_seleccionada = input (mensaje_pregunta)

while ( letra_seleccionada not in palabra_secreta) :
    print (mensaje_consolacion)
    letra_seleccionada = input (mensaje_pregunta)

print (mensaje_victoria.format(palabra_secreta)) 

#Si te extrañó la forma en el .format es para llenar un string cuando aparezcan estos simbolos {}
#con una variable

print ("hola solo demostraré algo interesante {} == {} y ademas 2 != {} aunque es obvio".format (2,2,4))








 



