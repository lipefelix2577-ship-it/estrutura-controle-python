'''
Você foi contrato para criar um menu interativo de mensagens de cumprimento.
 
Se o usuário entrar com a letra M ou palavra Manhã, deve mostrar a mensagem "Bom dia e o nome da pessoa!"
Se o usuário entrar com a letra T ou palavra Tarde, deve mostrar a mensagem "Boa tarde e o nome da pessoa!"
Se o usuãrio entrar com a letra N ou palavra Noite, deve mostrar a mensagem "Boa noite eo nome da pessoa!"

'''
turno = input("Digite o turno (M/T/N):")
nome = input("Digite o seu nome:")
match turno:
    case "M" | "Manha" | "Manhã":
        print(f"Bom dia, {nome}!")
    case "T" | "Tarde":
        print(f"Boa tarde, {nome}!")
    case "N" | "Noite":
        print(f"Boa noite, {nome}!")
    case _:
        print("Turno inválido. Por favor, digite M, T ou N.")