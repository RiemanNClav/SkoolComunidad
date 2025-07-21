#Expresiones Regulares. se opera el texto de la manera mas flexible
#Consulta de busqueda de texto que se expresa mediante un patrón de cadena, las expresiones regulares ayudan
#a responder preguntas como, ¿cuáles son todas las palabras de cuatro letras en un archivo?, 
#¿O cuántos tipos de error diferentes hay en este registro de errores?, 
#nos permiten buscar en un texto de cadenas que coincidan con un patrón en especifico.
#Podemos usar herramientas de líneas de comandos que sepan cómo aplicar expresiones regulares, como grep,sed y awk. 

#Ejemplo: Queremos extraer el identifiador de proceso de esta línea
log = 'July 31:07:51:48 my compudet bad_process[12345]: ERROR' 

#Metodo del índice para encontrar el primer corchete de la cadena
index = log.index('[')
print(log[index+1:index+6])
# Este método esta un poco limitado si el numero del indentificador cambia o si hay otro corchete antes. 

#Metodo de buscar Expresiónes Regulares dentro de las cadenas
import re
regex = r"\[(\d+)\]"
result =  re.search(regex,log)
print(result[1]) #Esto funciona siempre y cuando haya una secuencia de números en la cadena, marcada entre corchetes, 
                 # esa expresión regular extraerá esos números para nosotros. 


# BASIC MATCHING WITH GREP 
# Grep es una herramienta fácil de usar pero extremadamente potente para aplicar expresiones regulares
#manera de probar facilmente algunas expresiones regulares. 
# La mas simple de todas las coincidencias es solo buscar para ver si la cadena está presente, grep imprimirá 
# cualquier línea que contenga esa cadena en el archivo que le damos. 
#Equivalente de GREP para windows

#C:\Users\URIEL\Documents\CURSO PYTHON>findstr /i /r /c:"atabal" a.txt

# buscar una palabra tal que '.' pueda coincidir con cualquier caracter.
 
#C:\Users\URIEL\Documents\CURSO PYTHON>findstr /i "^arr.bal" a.txt
#arrabal
#arrabalero, ra
#arrobal
print(re.findall('b.d',log))

#Cuando el patrón no es una palabra completa
# Que empiezan con una palabra en particular. 
#C:\Users\URIEL\Documents\CURSO PYTHON>findstr /i "^arr" a.txt


 
