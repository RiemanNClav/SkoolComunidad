# GRUPOS DE CAPTURA
## grupos de captura son partes del patrón que están entre paréntesis.
import re 
result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada') #\w coincidirá con letra, números y guiones bajos. 
print(result.groups())
##añadiendo espacios y puntos al pattern de arriba
pattern = ^([\w .-]*], ([\w .-]*)


##si quisieramos un patrón que se repita un número específico de veces, python ofrece calificadores de repetición numéricos.
##se escriben entre corchetes y pueden ser de dos números que especifican un range. 
print(re.search(r"[a-zA-Z]{5}", 'a ghost'))
print(re.search(r"[a-zA-Z]{5}", 'a scary ghost appeared'))
print(re.findall(r"[a-zA-Z]{5}", 'a scary ghost appeared'))
##si quisieramos hacer coincidir todas las palabras que tienen exactamente cinco letras de largo?
print(re.findall(r"\b[a-zA-Z]{5}\b", 'a scary ghost appeared'))
##si quisieramos hacer coincidir en rangos de posiciones. 
print(re.findall(r"\w{5,10}", 'I really like strawberries'))
print(re.findall(r"\w{5,}", 'I really like strawberries'))

log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade' 
regex = r'\[(\d+)\]'
result = re.search(regex, log) #aqui extraeremos numeros que esten entre parentesis
print(result[1])
result = re.search(regex, 'A completely different string has numbers [34567]')

def extract_pid(log_line):
	regex = r"\[(\d+)\]"
	result = re.search(regex, log_line)
	if result is None:
		return ""
	return result[1]

print(extract_pid(log))

## FUNCION SPLIT
# Funciona similar a la que se usa con división de cadenas, tomando una expresión regular como división,
re.split(r'[.?!]'), 'One sentence, Another One?, And the last one!") 


## El segundo parametro lo utilizaremos para reemplazar la cadena coincidente, el \2\1 nos ayuda a invertir los grupos de captura. 
 re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada')







