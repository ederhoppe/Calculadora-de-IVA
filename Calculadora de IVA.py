"""
Ejercicio: Calculadora de IVA Automática.
Descripción: Este programa solicita un monto al usuario, calcula el 16% de IVA 
             y muestra el resultado formateado, permitiendo el uso de decimales.
"""

print("--- Calculadora de IVA (16%) ---")

monto = float(input("Ingresa el valor del producto: $"))
iva = monto * 0.16
total = monto + iva

print(f"El IVA aplicado es: ${iva:.2f}")
print(f"El total a pagar es: ${total:.2f}")
