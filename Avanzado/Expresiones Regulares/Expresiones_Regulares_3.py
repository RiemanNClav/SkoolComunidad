# PRACTICA 
.*n$ lineas que terminan con la n.

result = re.search(r'A.*a','Argentina')
print(result)

result = re.search(r'A.*a','Kazajistan')
print(result)

result = re.search(r'^A.*a$','Azerbaijan')
print(result)

result = re.search(r'^A.*a$','Australia')
print(result)

## ver si nuestros nombres de variables, son válidos, sabiendo que no deben de empezar con números y no pueden haber espacios.
pattern = r'^[a-zA-Z_][a-zA_Z0-9_]*$' 
result = re.search(pattern,'_Valid_variable_name')
print(result)

result = re.search(pattern,'_Valid variable name')
print(result)
