import sys
#creemos nuestro propio error

# cantidad_pasajeros = 10
# if cantidad_pasajeros > 5:
#     raise Exception(
#     'la cantidad de pasajeros no debe ser mayor a 5 usted ingresó {} '
#     .format(cantidad_pasajeros))

# Definir que solo corre sobre un sistema operativo
# assert ('linux' in sys.platform), "Este código corre solo en linux."

#extructura try except
def linux_interaction():
    assert ('linux' in sys.platform), "Esta fúncion solo se ejecutará en Linux."
    print('Si eres Linux este mensaje aparecerá en pantalla.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('La función linux_interaction() no fue ejecutada')

#Y si no existe un archivo?

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('no se puedo encontrar el archivo file.log')

#O podemos mostrar el error original detectado por python
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

#uniendo los dos casos

try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('La función linux_interaction() no fue ejecutada')

#la estructura finally se ejecutará al final sin importar que
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Esto se ejecuta siempre')
