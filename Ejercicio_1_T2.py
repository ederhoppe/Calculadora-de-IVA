"""1. El programa al iniciar debe presentar un mensaje de saludo y solicitarle al usuario que escriba una
cantidad de dinero. El programa deberá calcular el 16% de esa cantidad y presentar como 
resultados:
Tus resultados son: 
IVA al 16%: 
La cantidad sin IVA:
La cantidad con IVA:
Qué divertido es pagar impuestos!"""

print('Bienvenido a la calculadora de IVA 2.0')
cantidad_siniva = float(input('Ingrese la cantidad a calcular: '))
iva = cantidad_siniva*.16
cantidad_coniva = cantidad_siniva + iva
print('IVA al 16%:', iva)
print('La cantidad sin IVA:', cantidad_siniva)
print('La cantidad con IVA:', cantidad_coniva)
print('Que divertido es pagar impuestos!')