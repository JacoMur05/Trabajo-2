# Asignación de Variable
# numero = float(input("Ingrese un valor: "))

# Condicionales
# if numero == 1:
#     print("Verdadero")
# elif numero == 2:
#     print("Hola Mundo")
# else:
#     print("Falso")

# Bucles
# conteo = 0
# while conteo < 10:
#     conteo += 1
#     print("conteo")

# for i in range(0, 13, 2):
#     print(i)

# lista = ["Hola", 12, 1.2, True]

# print(lista)

# del(lista[1])

# print(lista)

nombres = []

def crear(nombre):
    if nombre == "Miguel":
        print('Ese nombre no se puede ingresar')
    else: 
        nombres.append(nombre)

crear('Jacobo')
crear('Miguel')

crear('Lina')
crear('Diana')
print(nombres)
