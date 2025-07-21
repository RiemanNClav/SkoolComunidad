¿Que es una prueba?
Sofware Testing es un proceso de evaluación de código informativo para determinar
si hace o no lo que espera que haga, Escribir pruebas puede ayudarle a eliminar un 
montón de errores, ayudando a mejorar la fiabilidad y la calidad de la automatización. 

Tarea de los programadores es probar codigo para asegurarse que se comporta de la manera 
que esperaban, ayudando asi a detectar errores. 
# Pruebas Manuales: Ejecutar un script con diferentes argumentos de linea de comandos. 
# Pruebas Atomaticas: Automatizar el proceso de comprobación de si el valor devuelvo coincide con las expectativas
                     # Escribir codigo para probar el codigo que se tiene. 

#UNIT TESTS
Se utilizan para verificar que las pequeñas partes aisladas de un programa son correctas,
generalmente se escriben junto con el codigo para probar el comportamiento, de piezas 
individuales o unidades como funciones o métodos, fragmento de cada codigo haga lo que deberia de hacer. 
Las pruebas automaticas generalmente se escriben junto con el codigo que queremos probar. 
para hacer las pruebas python tiene un modulo "unittest", contiene metodos para crear facilmente pruebas unitarias para el codigo. 

import unittest
class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = 'Lovelace, Ada' 
		expected = 'Ada, Lovelace'
		self.assertEqual(rearrange_name(testcase), expected) #verifica que lo es que esperaba es exacto lo que se obtuvo.

unittest.main()
Esto solo esta para una prueba, ¿Si quisieramos mas pruebas?

class TestRearrange(unittest.TestCase):

	def test_basic(self):
		testcase = 'Lovelace, Ada' 
		expected = 'Ada, Lovelace'
		self.assertEqual(rearrange_name(testcase), expected)
	def test_empty(self):
		testcase = ''
		expected = ''
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()


# Edge cases: los casos de borde son entradas a nuestro codigo que producen resultado inesperados. 
# se encuenran en los extremos de los rangos de entrada. 

nuestra prueba es Black Box o White Box?
WB es una prueba en donde el creador saber que tipos de casos puede validar y modificar el codigo fuente..
BB No se conocen los aspectos internos de como funciona el software

Integration Test
verifica que las interacciones entre los diferentes fragmentos de codigo en entornos
integrados funcionan de la manera que esperamos. 



