"""2. Calculadora de IVA (2)
El programa es una variante de la calculadora de iva original pero en esta ocasión el programa 
permite que el usuario también pueda decir a cuánto equivale el IVA"""

print('Bienvenido a la Calculadora de IVA 3.0')
cantidad_siniva = float(input('Ingresa una cantidad: '))
iva = float(input('Ingresa el valor del IVA: '))/100
iva_calcualdo = cantidad_siniva * iva
cantidad_coniva = cantidad_siniva + iva_calcualdo
print(f'IVA al {iva * 100}%:')
print('La cantidad sin IVA:', cantidad_siniva)
print('La cantidad con IVA:', cantidad_coniva)
print('Que divertido es pagar impuestos!')
