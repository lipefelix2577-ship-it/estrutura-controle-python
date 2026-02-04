while True:
    print("=== Menu de Atendimento ===")
    print("[1] Falar com atendente")
    print("[2] Segunda via de boleto")
    print("[3] Cancelar serviço")
    print("[4] Informações sobre planos")
    print("[5] Sair")

    opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":
            print("Você escolheu falar com um atendente. Aguarde...")
        case "2":
            print("Você escolheu segunda via de boleto.")
        case "3":
            print("Você escolheu cancelar serviço.")       
        case "4":
            print("Você escolheu informações sobre planos.")
        case "5":
            print("Saindo do menu. Obrigado!") 
            break
        case _:
            print("Opção inválida. Tente novamente.")