#python3
from time import sleep
from random import choice

palavras = ['hello word','dinheiro','vida','complexidade','inferior','gta','comida']

pontos = 0

jogas = 0

while True:
	jogas += 1
	ale = choice(palavras)
	print(20 * '-')
	print(ale)
	print(20 * '-')
	pergunta = input('PALAVRA: ')
	
	if pergunta == ale:
		print('você acertou!')
		pontos += 1

	if pergunta != ale:
		print('você errou!')

	if jogas == 10:
		pontos_perdidos = 10 - pontos
		print(20 * '-')
		print(f'você acertou {pontos} e errou {pontos_perdidos}')
		break
