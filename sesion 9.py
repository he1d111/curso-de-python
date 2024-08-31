import random
numero_aleatorio = random.random()
print(numero_aleatorio)

numero_aleatorio2 = random.randint(1,10)
print(numero_aleatorio2)

numero_aleatorio3 = random.uniform(1.0, 10.0)
print(numero_aleatorio3)

lista = ["Guitarra", "Bajo", "Bateria"]
random.shuffle(lista)
print(lista)

random_element = random.choice(lista)
print(random_element)