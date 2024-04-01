def calcular_suma_divisores(numero):
  suma_divisores = 0
  for i in range(1, numero):
      if numero % i == 0:
          suma_divisores += i
  return suma_divisores

def encontrar_numeros_perfectos_hasta_N(N):
  numeros_perfectos = []
  for num in range(1, N + 1):
      suma_divisores = calcular_suma_divisores(num)
      if suma_divisores == num:
          numeros_perfectos.append(num)
  return numeros_perfectos

def main():
  try:
      N = int(input("Ingrese el valor máximo:"))
      numeros_perfectos = encontrar_numeros_perfectos_hasta_N(N)
      if numeros_perfectos:
          print("Números perfectos hasta", N, ":")
          for numero in numeros_perfectos:
              print(numero)
      else:
          print("No se encontraron números perfectos", N)
  except ValueError:
      print("Error: Por favor, ingrese un número entero válido.")
  main()
