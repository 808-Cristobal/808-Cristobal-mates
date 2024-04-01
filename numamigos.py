def calcular_suma_divisores(numero):
  suma_divisores = 0
  for i in range(1, numero):
      if numero % i == 0:
          suma_divisores += i
  return suma_divisores

def amigos(num1, num2):
  suma_divisores_num1 = calcular_suma_divisores(num1)
  suma_divisores_num2 = calcular_suma_divisores(num2)
  return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

def main():
  try:
      num1 = int(input("Ingrese el primer número: "))
      num2 = int(input("Ingrese el segundo número: "))
      if amigos(num1, num2):
          print(num1, "y", num2, "son números amigos.")
      else:
          print(num1, "y", num2, "no son números amigos.")
  except ValueError:
      print("Error: Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
  main()
