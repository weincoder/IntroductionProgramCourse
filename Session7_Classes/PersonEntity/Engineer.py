#en este caso supongamos que un humano se especializó en
#ingenieria
import PersonEntity.Person as pers

class Engineer (pers.Person) :
    def __init__(self, nombre,profesion):
        self.profesion = profesion
        self.mensaje_humilde = "somos parecidos en habilidad mental por eso puedo decir que habla, el dice : {}"


    def reversed_message (self,message) :
        reversor =""
        for i in range (len(message)) :
            reversor += message[-(i+1)]
        return reversor

    def translate_alien (self,alienmessage) :
        print(self.mensaje_humilde.format(
            self.reversed_message(alienmessage)))

        