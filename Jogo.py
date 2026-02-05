'''
Fixar os conceitos de estruturas condicionais em Python (if/elif/else e match case) através de uma situação simulada de escolha e ação dentro de um jogo.
 
📋 Descrição da Tarefa:
 
Você está criando um pequeno sistema de um jogo de aventura onde o jogador será classificado por sua experiência e, com base em sua escolha, executará uma ação dentro do jogo.
 
🔧 O que seu programa deve fazer:
 
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):
 
Menos de 100 → "Iniciante"
 
Entre 100 e 500 → "Intermediário"
 
Mais de 500 → "Veterano"
 
Use if/elif/else para essa classificação.
 
2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case):
 
"A" → Atacar
 
"D" → Defender
 
"F" → Fugir
 
Qualquer outra tecla → "Ação inválida"
 
Mostre uma mensagem apropriada para cada ação, como:
 
"Você avançou para o ataque!"
 
"Você levantou o escudo!"
 
"Você fugiu da batalha!"
 
📝 Regras de Entrega:
Crie seu código em um arquivo .py
Faça testes com diferentes níveis de XP e ações
Envie o código por GitHub ou por sua plataforma de aulas
'''

Personagem = int(input("Digite seus pontos de experiência (XP): "))
if Personagem < 100:
    nivel = "Iniciante"
elif 100 <= Personagem <= 500:
    nivel = "Intermediário" 
else:
    nivel = "Veterano"              
print(f"Seu nível é: {nivel}")  
acao = input("Escolha uma ação (A: Atacar, D: Defender, F: Fugir): ")
match acao:         
    case "A":
        print("Você avançou para o ataque!")
    case "D":
        print("Você levantou o escudo!")
    case "F":
        print("Você fugiu da batalha!")
    case _:
        print("Ação inválida!!")
        