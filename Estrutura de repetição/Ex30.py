#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, 
#a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
print('_'*30)
q_paes = int(input("Digite a quantidade de paes desejados:"))
print("Panificadora Pão de Ontem - Tabela de Preços")

for c in range(1,q_paes+1):
    print(f"{c} - R$ {c * 0.18:.2f}")