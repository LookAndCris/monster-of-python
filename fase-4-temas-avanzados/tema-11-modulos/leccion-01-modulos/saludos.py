# Este es un módulo con funciones que saludan
def saludar_de_noche():
	print("Buenoas noches")

def saludar_de_dia():
	print("Buenos dias")

class Saludo():
	def __init__(self):
		print("Hola, te estoy saludando desde el __init__ de la clase Saludo")

# Esto es para que se ejecute el archivo como script y no como módulo.
if __name__ == '__main__':
	saludar_de_dia()
	saludar_de_noche()
	Saludo()