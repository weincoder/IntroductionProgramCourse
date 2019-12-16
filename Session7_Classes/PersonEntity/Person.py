#Ahora observemos las clases estas son entidades
#con funciones bien definidas
#por ejemplo una persona
class Person :
    #Esta función se ejecuta en el momento de crear un objeto del tipo persona
    #Siempre será la función que se ejecute de primero al crear un objeto
    #de una clase
    def __init__(self,nombre):
        #Self sirve para acceder y configurar los atrubutos de la clase
        #en este caso se define el atributo nombre, message_preview,message_walk
        self.nombre = nombre
        self.message_preview ="Hola mi nombre es {} y tengo un mensaje quedar : \n{}"
        self.message_walk="estoy dando mi paso {} y caminare hasta {} pasos"
        #Este mensaje se mostrará siempre al crear una nueva entidad persona
        print ("Soy una persona nueva, mi nombre es {}".format(self.nombre))

    def talk (self,message) :
        print (self.message_preview.format(self.nombre,message))

    def walk_n_steps(self,n_steps) :
        for i in range (n_steps) : print(self.message_walk.format (i+1,n_steps))
