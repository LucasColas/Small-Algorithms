import random

nombre_aleatoire = random.randint(1,10)

for x in range(3):
	nombre = int(input ("Enter a number : "))

	if nombre == nombre_aleatoire:
		print("You won!")
		break

	if nombre > nombre_aleatoire: 
		print("Your number is too large !")

	if nombre < nombre_aleatoire:
		print("Your number is too small!")


if nombre != nombre_aleatoire:
	print("You lost !")
	print("It was : ", end='')
	print(nombre_aleatoire)
