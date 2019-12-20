import PersonEntity.Person as Per
import AlienEntity.Alien as Ali
import PersonEntity.Engineer as eng

alien_mensaje = "etnatsni olos nu ne sosap 4 a yov areiuq euq adanedroc al a otropsnartelet em onimac on oy"
#Al igual que las funciones se deben importar
#no obstante deben iniciarse con las variables 
#configuradas en el init, por eso para el caso de persona
#solo require del nombre
#Y del alien pide el nombre y el planeta
mafer = Per.Person ("mafer")
mafer.talk("Esto realmente funciona muy bien")
mafer.walk_n_steps (4)
rodolfo = Ali.Alien("rodolfo", "marte")
rodolfo.talk ("yo hablo al contrario de lo que crees")
rodolfo.walk_n_steps(4)
daniel = eng.Engineer("daniel", "ingenierio biomédico")
daniel.translate_alien (alien_mensaje)
