class ManipuladorDeArquivos:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def criar_arquivo(self):
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write('')
        print('\nArquivo criado com sucesso.')

    def ler_arquivo(self, modo='r'):
        try:
            with open(self.nome_arquivo, modo) as arquivo:
                return arquivo.read()
        except FileNotFoundError:
            print(f"\nArquivo {self.nome_arquivo} não encontrado.")
            return None

    def editar_arquivo(self, novo_conteudo, modo='a'):
        try:
            with open(self.nome_arquivo, modo) as arquivo:
                arquivo.write(novo_conteudo)
            print(f"\nConteúdo do arquivo {self.nome_arquivo} atualizado.")
        except FileNotFoundError:
            print(f"\nArquivo {self.nome_arquivo} não encontrado.")

    def reescrever_arquivo(self, novo_conteudo):
        self.editar_arquivo(novo_conteudo, modo='w')


try:
    while True:
        print('')
        menu = int(input('Digite o número da opção:\n \
            1- Criar arquivo\n \
            2- Ler Arquivo\n \
            3- Editar Arquivo\n \
            4- Reescrever arquivo\n \
            5- Sair \n'))
        
        
        if menu == 5:
            exit()

        caminho_arquivo = input('Digite o caminho e/ou nome do arquivo: \n')
            
        arquivo = ManipuladorDeArquivos(caminho_arquivo)
        
        match menu:
            case 1:
                arquivo.criar_arquivo()
            case 2:
                conteudo = arquivo.ler_arquivo()
                print(conteudo)
            case 3:
                texto = input('\nDigite o texto que deseja adicionar: ')
                arquivo.editar_arquivo(texto)
            case 4:
                texto = input('\nDigite o texto que deseja adicionar: ')
                arquivo.reescrever_arquivo(texto)
            case _:
                print('\nOpção Inválida')
                
except:
    print('Você finalizou o programa ou ocorreu um erro.')