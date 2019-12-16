class Alien:
    def __init__(self,nombre,planeta):
        self.nombre = nombre
        self.planeta = planeta
        self.message_preview =": radeuq ejasnem nu ognet y {} se erbmon im aloh \n{}"
        self.message_walk="yo no camino me teletransporto a la cordenada que quiera voy a {} paso en un solo instante"
        #Este mensaje se mostrará siempre al crear una nueva entidad persona
        print ("{} atetnalp led yos {} se erbmon im ,oveun neila nu yos".format(
            self.reversed_message(self.planeta), 
            self.reversed_message(self.nombre)))
    def reversed_message (self,message) :
        reversor =""
        for i in range (len(message)) :
            reversor += message[-(i+1)]
        return reversor
    def talk (self,message) :
        print (self.message_preview.format(
            self.nombre,self.reversed_message(message)))
    #podemos llamar funciones de la misma clase empleando self. nombre de la 
    #función
    def walk_n_steps(self,n_steps) :
        self.talk(self.message_walk.format (n_steps))



