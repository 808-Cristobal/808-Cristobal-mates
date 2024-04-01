def calcular_coeficiente(fila, columna):
  if columna == 0 or columna == fila:
      return 1
  else:
      return calcular_coeficiente(fila - 1, columna - 1) + calcular_coeficiente(fila - 1, columna)

def generar_triangulo_pascal(n):
  triangulo = []
  for fila in range(n):
      fila_tri = []
      for columna in range(fila + 1):
          fila_tri.append(calcular_coeficiente(fila, columna))
      triangulo.append(fila_tri)
  return triangulo

def imprimir_triangulo_pascal(triangulo):
  for fila in triangulo:
      print(" ".join(str(elemento) for elemento in fila).center(80))

def main():
  try:
      n = int(input("Ingrese el número de filas: "))
      triangulo = generar_triangulo_pascal(n)
      imprimir_triangulo_pascal(triangulo)
  except ValueError:
      print("Error: Por favor, ingrese un número entero")

if __name__ == " Menú ":
  main()
