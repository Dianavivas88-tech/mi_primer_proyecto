print("Calculadora básica")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Operación (+, -, *, /): ")
 
if operacion == '+':
   print("Resultado:", a + b)
elif operacion == '-':
   print("Resultado:", a - b)
elif operacion == '*':
   print("Resultado:", a * b)
elif operacion == '/':
   if b != 0:
       print("Resultado:", a / b)
   else:
       print("Error: no se puede dividir entre cero.")
else:
   print("Operación no válida.")