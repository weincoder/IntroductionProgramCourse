#Comencemos definiendo los condicionales comunes
#En este caso estamos preguntando por la igualdad de dos variables
print(8==8, "hola"=="kio",3==1,"daniel"=="daniel")
#Python nos retornará en caso de verdadero True de lo contrario False

#En el siguiente caso tenemos para preguntar diferente
print(8!=2)

#Mayor que , Menor que
print(8>2, 4<2,8>=2,2<=2)

#Tambien podemos preguntar si una porción de texto esta en otra
# empleando el condicional in y en caso de preguntar de que no: not in
print("a" in "hola", "hola" not in "hola mundo como estas?")


#Teniendo esto presente podemos evaluar los condicionales 

#Un condicional me pregunta si un escenario esta acontenciendo
#y a partir de esto tomas acciones. Por ejemplo si un computador vale 2000 dolares
#la pregunta es si tengo suficiente dinero

dinero=2100

if (dinero>=2000):
    print("te puedes comprar el computador!!! te sobra : ",dinero-2000,"pesos")
    print("estoy bien identado solo me muestro cuando se cumple la condición")   
print("siembre me ejecutare")
#En el caso anterio if indica la pregunta, el contenido de los parentesis la pregunta y el dos puntos
#indica que cuando se cumpla la condición se debe ejecutar lo que esta debajo. Para indicar que 
#las acciones que deseamos ejecutar que siempre que se cumpla este if deben estar identadas debajo del
#condicional, de forma que el primer y el segundo print solo se mostraran cuando se cumpla la condición
#sin embargo el tercero siembre se ejecutará


#tambien existe la posibilidad de preguntar algo adicional en caso de que la primera condición no se cumpla
#para ello hagamos el ejemplo que deseamos saber quien es mayor un numero A o B

numero_a = 2
numero_b = 4

if (numero_a > numero_b):
    print ("el numero mayor es el A")
elif (numero_b > numero_a):
    print("el numero mayor es el B") 
else:
    print("son iguales nada que hacer")


#para este caso elif hace referencia a que si una anterior condición no es cumplida puedo hacer otra pregunta
#esto es interesante pues podemos hacer muchas preguntas para llegar a una respuesta. En caso de que no quede 
#ninguna otra opción podemos poner else. por ejemplo, en el caso anterior no era necesario preguntar si (a==b)
#ya que era la única posibilidad que quedaba
