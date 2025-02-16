#12.	Encontrar el mayor entre tres numeros dados.
print("Ingrese tres numeros a su eleccion y se le dira el mayor de ellos")
nume1 = int(input("ingrese el primer numero:"))
nume2 = int(input("Ingrese el segundo numero:"))
nume3 = int(input("Ingrese el tercer numero<."))
if nume1>nume2 and nume1>nume3:
    print(f"El numero mayor es: {nume1}")
elif nume2>nume1 and nume2>nume3:
    print(f"El numero mayor es: {nume2}")
else:
    print(f"El numero mayor es: {nume3}")
  


