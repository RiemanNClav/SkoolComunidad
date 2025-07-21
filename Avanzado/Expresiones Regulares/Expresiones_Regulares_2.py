# EXPRESIONES REGULARES BASICAS 
import re 
result = re.search(r'aza','plaza')
print(result)
result_2 = re.search(r'aza','computadoraza')
print(result_2)
result_3 = re.search(r'aza', 'azadas')
print(result_3)
##Si no hay coincidencia, el ouput es 'None', significa que no encontro coincidencia. 
##Buscas caracteres al principio:
result_4 = re.search(r'^Xenos','Xenostian')
print(result_4)
##Para que la coincidencia no distinga entre mayusculas y minusculas:
result_5 = re.search(r'^x.nos','Xenostian', re.IGNORECASE)

## CLASES DE CARACTERES
##se escriben entre corchetes
result = re.search(r'[Pp]ython','Python')
print(result)
##podemos definir un rango de caracteres usando un guión:
result = re.search(r'[a-z]way','The end of the highway')
print(result)

result = re.search(r'cloud[a-zA-Z0-9]','cloudy')
print(result)

result = re.search(r'cloud[a-zA-Z0-9]','cloud9')
print(result)

result = re.search(r'cloud[a-zA-Z0-9]','cloudY')
print(result)

result = re.search(r'cloud[a-zA-Z0-9]','cloudA')
print(result)

## Para buscar cualquier caracter que no sea una letra, coincidiendo con el primer espacio.
result = re.search(r'[^a-zA-Z]','Sentence with spaces.')
print(result)

## Buscar cualquier caracter que no sea una letra y un espacio.
result = re.search(r'[^a-zA-Z ]','Sentence with spaces.')
print(result)

## Que coincida con una palabra o con otra:
result = re.search(r'cat|dog','I like cats.')
print(result)

## Encuentre todos los resultados:
result = re.findall(r'cat|dos','I like both dogs and cats.')
print(result)

## COINCIDENCIAS REPETIDAS
.*n = se expande hasta la ultima n de la cadena de caracteres.
+ = coincide con una o más ocurrencias del carácter anterior, de manera consecutiva
? = Significa cero o una ocurrencia del carácter anterior


#--------------------------------------------------------------------------------------
result = re.search(r'Py.*n','Pygmalion') # se puede leer como ' py + caulquier numero de otros caracteres seguidos de n.
print(result)

result = re.search(r'Py.*n','Python Programming')
print(result)

result = re.search(r'Py[a-z]*n','Python Programming')
print(result)

result = re.search(r'o+l+','goldfish')
print(result)

result = re.search(r'o+l+','woolly')
print(result)

result = re.search(r'p?each','To each their own.')
print(result)

result = re.search(r'p?each','I like peaches.')
print(result)


# CARACTER ESCAPE 
\w* = coincide con cualquier caracter alfanumerico, incluyendo letras, numeros y guiones bajos
\d = coincidencias de digitos. 
\s = para caracteres de espacio en blanco como espacio, tabulación o nueva linea.
\b = limite de palabras.
\d+ = coincidir con uno o más caracteres numéricos. 
# ----------------------------------------------------------------------

result = re.search(r'/.com','welcome')
print(result)

result = re.search(r'/.com','Had.com')
print(result)

##\w coincide con letras,números y guiones bajos 
result = re.search(r'\w*','And_this_is_another')
print(result)




