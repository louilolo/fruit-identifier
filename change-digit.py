import os

def alterar_primeiro_digito(arquivo, novo_numero):
    linhas_alteradas = []
    with open(arquivo, 'r') as f:
        for linha in f:
            if linha.strip():  # Ignora linhas em branco
                nova_linha = str(novo_numero) + linha[1:]
                linhas_alteradas.append(nova_linha)

    with open(arquivo, 'w') as f:
        for linha in linhas_alteradas:
            f.write(linha)

def main():
    pasta = "C:Users\\dhomi\\OneDrive\\Área de Trabalho\\test\\obj_train_data"  # Substitua pelo caminho real da pasta
    novo_numero = 2  # Substitua pelo número desejado

    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            alterar_primeiro_digito(caminho_arquivo, novo_numero)
            print(f'Arquivo {arquivo} processado.')

if __name__ == "__main__":
    main()
