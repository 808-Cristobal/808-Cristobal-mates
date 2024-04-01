def calcular_mcd(a, b):
  while b != 0:
      a, b = b, a % b
  return a

def main():
  try:
      num1 = int(input("Ingrese el primer número: "))
      num2 = int(input("Ingrese el segundo número: "))

      mcd = calcular_mcd(num1, num2)

      print("El MCD de", num1, "y", num2, "es:", mcd)
  except ValueError:
      print("Error: Por favor, ingrese solo números enteros.")

if __name__ == " Menú ":
  main()
