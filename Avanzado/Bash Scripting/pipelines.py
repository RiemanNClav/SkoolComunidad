#Redirección: Proceso de envío de una secuencia a un destino diferente, proceso proporcionado
# por el sistema operativo y puede ser realmente util cuando desea almacenar la salida de un 
# comando en un archivo. 
#print('Dont mind me') -> cat example.py #sin redirección, el texto se enviará a la pantalla utilizando el STD fuera. 
#example.py > new_file.txt

#PIPES AND PIPELINES
#Conectar varios scripts, comandos en una canalización de procesamiento de datos, 
#Las tuberías conectan la salida de un programa a la entrada de otro, pasar datos 
#entre programas, tomando la salida de uno, conviertiendolo en la entrada de otro.

import sys 
for line in sys.stdin:
	print(line.strip().capitalize()) 

#ahora usaremos un script para capitalizar un archivo que tenemos en nuestro ordenador llamado Haiku.txt
