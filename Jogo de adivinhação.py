# NOME: LUCAS DANIEL DOS SANTOS ROSA
# SALA: 1B
import random   # importa a biblioteca random para gerar números aleatórios.
sorteio = random.randint(1, 100) # gera um único número aleatório para o código inteiro.
while True:
    chute = int(input("Tente adivinhar um número de 1 até 100!!! \nEscreva aqui seu número:"))
    if chute < sorteio:
        print(f"vixi.... quando você escolheu {chute} era menor do que o número que eu tinha sorteado, desiste não!!!")
    elif chute > sorteio:
        print(f"Ok... tente chutar menos do que {chute}. Não desista!")    
    else:
        print(f"Parabéns! Você acertou o número {sorteio}!")
        exit() # finaliza o programa quando o usuário acertar. Assim ele pode ter um novo número para tentar adivinhar quando reiniciar.