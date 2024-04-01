def es_numero_perfecto(numero):
  suma_divisores = 0
  for i in range(1, numero):
      if numero % i == 0:
          suma_divisores += i
  return suma_divisores == numero

def main():
  try:
      numero = int(input("Ingrese un número: "))
      if es_numero_perfecto(numero):
          print(numero, "es un número perfecto.")
      else:
          print(numero, "no es un número perfecto.")
  except ValueError:
      print("Error: Por favor, ingrese un número entero ")

if __name__ == "__main__":
  main()
